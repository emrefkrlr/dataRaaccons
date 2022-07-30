from __future__ import absolute_import, unicode_literals
from asyncio.log import logger
from celery import shared_task
import logging
from datetime import datetime
from crawlers.service import CrawlerServices
from activities.service import ActivitiesService
from mongo.services import MongoService
from products.service import ProductsService
from products.models import Products
from companies.models import Companies
from activities.models import Activities, ActivityCategory
from products.product_matches import jaro_winkler_distance


logger = logging.getLogger(__name__)

@shared_task
def insert_new_products_task():

    try:
        
        now = datetime.now()
        print("Celery insert_new_products_task started....", now)

        # get activities data on postgresql
        activities = ActivitiesService().get_all_activities()

        for activity in activities:
            
            # get crawlers data on postgresql
            crawlers = CrawlerServices().fetch_urls_to_crawl(filter={'status': 1, 'activity': activity.id})
        
            for crawler in crawlers:

                # latest mongo data by category retrieved from scraper
                query = {"info.company_name": str(crawler.company), "info.page_category": str(crawler.page_category)}

                get_mongo_data = MongoService().find_one(db_name='DataRaccoons', host='dataRaccoonsMongo', port='27017', 
                username='root', password='root', collection=str(activity.name), query=query)

                # get products on postgresql
                products = ProductsService().get_products(filter={'company__name': str(crawler.company), 'activity': activity.id, 'activity_category': ActivityCategory.objects.get(name=crawler.activity_category).id, 'status': 1})

                # find new products and save them in product table
                if get_mongo_data is not None and get_mongo_data["products_and_price"] is not None and len(get_mongo_data["products_and_price"]) > 0 :
                    
                    # If table is empty, add products without checking
                    if len(products) == 0:

                        for product_and_price in get_mongo_data["products_and_price"]:
                            
                            #for data from paging
                            if type(product_and_price) is list and product_and_price is not None:

                                for product_info in product_and_price:

                                    ProductsService().insert_new_products(
                                        company = Companies.objects.get(name=crawler.company),
                                        activity = Activities.objects.get(name=crawler.activity),
                                        activity_category = ActivityCategory.objects.get(name=crawler.activity_category),
                                        product_name = product_info["product_name"],
                                        price = product_info["price"],
                                        page_category = str(crawler.page_category),
                                        sub_category = product_info["sub_category"] if product_info["sub_category"] else None,
                                        product_url = product_info["product_url"] if product_info["product_url"] else None,
                                        image = product_info["image"] if product_info["image"] else None
                                    )

                            #for data from not paging    
                            else:

                                if product_and_price is not None:
                                    
                                    # insert data
                                    ProductsService().insert_new_products(
                                        company = Companies.objects.get(name=crawler.company),
                                        activity = Activities.objects.get(name=crawler.activity),
                                        activity_category = ActivityCategory.objects.get(name=crawler.activity_category),
                                        product_name = product_and_price["product_name"],
                                        price = product_and_price["price"],
                                        page_category = str(crawler.page_category),
                                        sub_category = product_and_price["sub_category"] if product_and_price["sub_category"] else None,
                                        product_url = product_and_price["product_url"] if product_and_price["product_url"] else None,
                                        image = product_and_price["image"] if product_and_price["image"] else None
                                    )

                    # If table is not empty, add products without checking           
                    else:

                        for product_and_price in get_mongo_data["products_and_price"]:
                            
                            #for data from paging
                            if type(product_and_price) is list and product_and_price is not None:

                                for product_info in product_and_price:

                                    if product_info["product_name"] not in products:

                                        ProductsService().insert_new_products(
                                            company = Companies.objects.get(name=crawler.company),
                                            activity = Activities.objects.get(name=crawler.activity),
                                            activity_category = ActivityCategory.objects.get(name=crawler.activity_category),
                                            product_name = product_info["product_name"],
                                            price = product_info["price"],
                                            page_category = str(crawler.page_category),
                                            sub_category = product_info["sub_category"] if product_info["sub_category"] else None,
                                            product_url = product_info["product_url"] if product_info["product_url"] else None,
                                            image = product_info["image"] if product_info["image"] else None
                                        )
                                    
                                    else:

                                        ProductsService().update_or_create_products(price = product_info["price"])   

                            # for data from not paging
                            else:

                                if product_and_price is not None:                                  

                                    if product_and_price["product_name"] not in products:

                                        ProductsService().insert_new_products(
                                            company = Companies.objects.get(name=crawler.company),
                                            activity = Activities.objects.get(name=crawler.activity),
                                            activity_category = ActivityCategory.objects.get(name=crawler.activity_category),
                                            product_name = product_and_price["product_name"],
                                            price = product_and_price["price"],
                                            page_category = str(crawler.page_category),
                                            sub_category = product_and_price["sub_category"] if product_and_price["sub_category"] else None,
                                            product_url = product_and_price["product_url"] if product_and_price["product_url"] else None,
                                            image = product_and_price["image"] if product_and_price["image"] else None
                                        )
                                    else:

                                        ProductsService().update_or_create_products(price = product_and_price["price"])
                                    
                else:
                    continue
                    

        print("Celery insert_new_products_task done....", now)

    except Exception as e:
        print("\ninsert_new_products_task Exeption: \n{}".format(e))


@shared_task
def product_matches_task():

    try:

        now = datetime.now()
        print("Celery product_matches_task started....", now)

        # get activities data on postgresql
        activities = ActivitiesService().get_all_activities()

        for activity in activities:
            # get products on postgresql
            products = ProductsService().get_products(filter={'status':1, 'activity': activity.id})    

            for first in products:

                # fetch to check all products except current one
                check_product = ProductsService().exclude(first.id)
                
                for second in check_product:

                    # jaro winkler calculate score
                    score = jaro_winkler_distance.get_jaro_distance(first.product_name, second.product_name, winkler=True)
                
                    if score > 0.87:
                        
                        insert = ProductsService().insert_product_matches(
                            # FIRST PRODUCT INFO
                            first_product_activity_category_id = ActivityCategory.objects.get(name=first.activity_category).id,
                            first_company_id = Companies.objects.get(name=first.company).id,
                            first_product_id = first.id,
                            first_product_name = first.product_name,
                            
                            # SECOND PRODUCT INFO
                            second_product_activity_category_id = ActivityCategory.objects.get(name=second.activity_category).id,
                            second_company_id = Companies.objects.get(name=second.company).id,
                            second_product_id = second.id,
                            second_product_name = second.product_name,
                            
                            # MATCHED INFO
                            matches_activity = activity,
                            matched_score = score
                            )
                    
                        if insert is not True:
                            raise Exception('insert_new_products_task Exception: Postgre insert failed \n First Product: {} \n Second Product: {} \nActivity: {} \n '.format(first.second_product_id, second.second_product_id,activity))

        print("Celery product_matches_task done....", now)


    except Exception as e:
        print("\product_matches_task Exeption: \n{}".format(e))
