from __future__ import absolute_import, unicode_literals
from asyncio.log import logger
from celery import shared_task
import datetime

from products.service import ProductsService
from companies.service import CompaniesService
from activities.service import ActivitiesService
from mongo.services import MongoService

@shared_task
def dashbord_descriptive_statistics_task():
    
    activity_based_descriptive_statistics()
    activity_category_based_descriptive_statistics()
    #company_based_activity_category_descriptive_statistics()
    #company_based_activity_sub_category_descriptive_statistics()
    companies_all_statistics()


@shared_task
def activity_based_descriptive_statistics():

    print("activity_based_descriptive_statistics task started...")

    dashboard_data = {
        "name": "activity_based_descriptive_statistics",
        "time": str(datetime.datetime.now()),
        "data": []
    }

    activities = ActivitiesService().get_all_activities()

    for activity in activities:

        product_data = ProductsService().get_activity_descriptive_statistics(activity=activity)

        company_data = CompaniesService().get_companies_by_activity(activity=activity).count() if CompaniesService().get_companies_by_activity(activity=activity) else 0

        activity_data = {
            
            "activity": str(activity),
            "statistics": [{
                "company_count": company_data,
                "product_count": product_data["price__count"],
                "product_min_price": round(product_data["price__min"], 3) if product_data["price__min"] else 0,
                "product_max_price": round(product_data["price__max"], 3) if product_data["price__max"] else 0,
                "product_avg_price": round(product_data["price__avg"], 3) if product_data["price__avg"] else 0

            }]
        }

        dashboard_data["data"].append(activity_data)

    mongo = MongoService().insert_one(collection="dashboard", document=dashboard_data)

    if mongo:

        print("activity_based_descriptive_statistics document saved...")
    
    else:

        print("activity_based_descriptive_statistics document error...")



def activity_category_based_descriptive_statistics():

    print("activity_category_based_descriptive_statistics task started...")

    dashboard_data = {
        "name": "activity_category_based_descriptive_statistics",
        "time": str(datetime.datetime.now()),
        "data": []
    }

    activities = ActivitiesService().get_all_activities()

    for activity in activities:

        activity_data = {
            "activity": str(activity),
            "statistics": []
        }

        activity_categories = ActivitiesService().get_activity_categories(activity=activity)

        if activity_categories:

            for activity_category in activity_categories:

                activity_category_data = ProductsService().get_activity_category_descriptive_statistics(activity=activity, activity_category=activity_category)

                company_data = ProductsService().get_companies(activity=activity, activity_category=activity_category)

                activity_data["statistics"].append(
                    {    
                        "activity_category": str(activity_category),
                        "company_count": company_data.count() if company_data else 0,
                        "product_count": activity_category_data["price__count"],
                        "product_min_price": round(activity_category_data["price__min"], 3) if activity_category_data["price__min"] else 0,
                        "product_max_price": round(activity_category_data["price__max"], 3) if activity_category_data["price__max"] else 0,
                        "product_avg_price": round(activity_category_data["price__avg"], 3) if activity_category_data["price__avg"] else 0
                    }
                )

        dashboard_data["data"].append(activity_data)

    mongo = MongoService().insert_one(collection="dashboard", document=dashboard_data)

    if mongo:

        print("activity_category_based_descriptive_statistics document saved...")
    
    else:

        print("activity_category_based_descriptive_statistics document error...")



def company_based_activity_category_descriptive_statistics():

    print("company_based_activity_category_descriptive_statistics task started...")

    dashboard_data = {
        "name": "company_based_activity_category_descriptive_statistics",
        "time": str(datetime.datetime.now()),
        "data": []
    }

    activities = ActivitiesService().get_all_activities()

    for activity in activities:

        activity_data = {
            "activity": str(activity),
            "statistics": []
        }
        
        companies = CompaniesService().get_companies_by_activity(activity=activity)
        activity_categories = ActivitiesService().get_activity_categories(activity=activity)

        if companies and activity_categories:

            for company in companies:

                company_statistics = {
                    "company": CompaniesService().get_company_by_id(company=company.id).name,
                    "data": []
                }
               
                for activity_category in activity_categories:
                    
                    company_data = ProductsService().get_company_activity_category_descriptive_statistics(activity=activity, activity_category=activity_category, company=company.id)

                    company_statistics["data"].append(

                        {   
                            "activity_category": str(activity_category),
                            "product_count": company_data["price__count"],
                            "product_min_price": round(company_data["price__min"], 3) if company_data["price__min"] else 0,
                            "product_max_price": round(company_data["price__max"], 3) if company_data["price__max"] else 0,
                            "product_avg_price": round(company_data["price__avg"], 3) if company_data["price__avg"] else 0
                        }

                    )

                activity_data["statistics"].append(company_statistics)
                    
        dashboard_data["data"].append(activity_data)
    
    mongo = MongoService().insert_one(collection="dashboard", document=dashboard_data)

    if mongo:

        print("company_based_activity_category_descriptive_statistics document saved...")
    
    else:

        print("company_based_activity_category_descriptive_statistics document error...")


  
def company_based_activity_sub_category_descriptive_statistics():

    print("company_based_activity_sub_category_descriptive_statistics task started...")

    dashboard_data = {
        "name": "company_based_activity_sub_category_descriptive_statistics",
        "time": str(datetime.datetime.now()),
        "data": []
    }

    activities = ActivitiesService().get_all_activities()

    for activity in activities:

        activity_data = {
            "activity": str(activity),
            "statistics": []
        }
        
        companies = CompaniesService().get_companies_by_activity(activity=activity)
        activity_categories = ActivitiesService().get_activity_categories(activity=activity)

        if companies and activity_categories:

            for company in companies:

                company_statistics = {
                        "company": CompaniesService().get_company_by_id(company=company.id).name,
                        "data": []
                    }
               
                for activity_category in activity_categories:

                    activity_category_statistics = {
                        "activity_category": str(activity_category),
                        "data": []
                    }

                    activity_sub_categories = ActivitiesService().get_activity_sub_categories(activity_category=activity_category)

                    for activity_sub_category in activity_sub_categories:

                        activity_sub_category_data = ProductsService().get_company_activity_sub_category_descriptive_statistics(activity=activity, activity_category=activity_category, activity_sub_category=activity_sub_category, company=company.id)

                        activity_category_statistics["data"].append(
                            {   
                                "activity_sub_category": str(activity_sub_category),
                                "product_count": activity_sub_category_data["price__count"],
                                "product_min_price": round(activity_sub_category_data["price__min"], 3) if activity_sub_category_data["price__min"] else 0,
                                "product_max_price": round(activity_sub_category_data["price__max"], 3) if activity_sub_category_data["price__max"] else 0,
                                "product_avg_price": round(activity_sub_category_data["price__avg"], 3) if activity_sub_category_data["price__avg"] else 0
                            }
                        )
                
                    company_statistics["data"].append(activity_category_statistics)
        
                activity_data["statistics"].append(company_statistics)
    
        dashboard_data["data"].append(activity_data)
    
    mongo = MongoService().insert_one(collection="dashboard", document=dashboard_data)

    if mongo:

        print("company_based_activity_sub_category_descriptive_statistics document saved...")
    
    else:

        print("company_based_activity_sub_category_descriptive_statistics document error...")



def companies_all_statistics():

    print("companies_all_statistics task started...")

    dashboard_data = {
        "name": "companies_all_statistics",
        "time": str(datetime.datetime.now()),
        "data": []
    }

    activities = ActivitiesService().get_all_activities()

    for activity in activities:

        activity_data = {
            "activity": str(activity),
            "statistics": []
        }
        
        companies = CompaniesService().get_companies_by_activity(activity=activity)
        activity_categories = ActivitiesService().get_activity_categories(activity=activity)

        if companies and activity_categories:

            for company in companies:

                activity_data_statistics = ProductsService().get_company_activity_descriptive_statistics(activity=activity, company=company.id)

                company = CompaniesService().get_company_by_name(company=company)
                
                company_statistics = {
                    "company": company.name,
                    "company_name": company.page_name,
                    "logo": company.logo,
                    "product_count": activity_data_statistics["price__count"],
                    "product_min_price": round(activity_data_statistics["price__min"], 3) if activity_data_statistics["price__min"] else 0,
                    "product_max_price": round(activity_data_statistics["price__max"], 3) if activity_data_statistics["price__max"] else 0,
                    "product_avg_price": round(activity_data_statistics["price__avg"], 3) if activity_data_statistics["price__avg"] else 0,
                    "activity_categories_data": []
                }
               
                for activity_category in activity_categories:

                    activity_category = ActivitiesService().get_activity_category_by_name(activity_category=activity_category)

                    activity_data_statistics = ProductsService().get_company_activity_category_descriptive_statistics(activity=activity, activity_category=activity_category, company=company.id)

                    activity_category_statistics = {
                        "activity_category": str(activity_category),
                        "product_count": activity_data_statistics["price__count"],
                        "product_min_price": round(activity_data_statistics["price__min"], 3) if activity_data_statistics["price__min"] else 0,
                        "product_max_price": round(activity_data_statistics["price__max"], 3) if activity_data_statistics["price__max"] else 0,
                        "product_avg_price": round(activity_data_statistics["price__avg"], 3) if activity_data_statistics["price__avg"] else 0,
                        "activity_sub_categories_data": []
                    }

                    activity_sub_categories = ActivitiesService().get_activity_sub_categories(activity_category=activity_category)

                    for activity_sub_category in activity_sub_categories:

                        activity_sub_category = ActivitiesService().get_activity_sub_category_by_name(activity=activity, activity_category=activity_category, activity_sub_category=activity_sub_category)

                        if activity_sub_category.name == "check":

                            activity_sub_category_data = ProductsService().get_company_activity_sub_category_descriptive_statistics(activity=activity, activity_category=activity_category, activity_sub_category=1, company=company)
                        
                        else:

                            activity_sub_category_data = ProductsService().get_company_activity_sub_category_descriptive_statistics(activity=activity, activity_category=activity_category, activity_sub_category=activity_sub_category, company=company)
                        
                        activity_sub_category_statistic = {
                        
                            "activity_sub_category": str(activity_sub_category),
                            "product_count": activity_sub_category_data["price__count"],
                            "product_min_price": round(activity_sub_category_data["price__min"], 3) if activity_sub_category_data["price__min"] else 0,
                            "product_max_price": round(activity_sub_category_data["price__max"], 3) if activity_sub_category_data["price__max"] else 0,
                            "product_avg_price": round(activity_sub_category_data["price__avg"], 3) if activity_sub_category_data["price__avg"] else 0,

                        }

                        activity_category_statistics["activity_sub_categories_data"].append(activity_sub_category_statistic)

                    company_statistics["activity_categories_data"].append(activity_category_statistics)
                
                activity_data["statistics"].append(company_statistics)
        
        dashboard_data["data"].append(activity_data)
    
    mongo = MongoService().insert_one(collection="dashboard", document=dashboard_data)

    if mongo:

        print("companies_all_statistics document saved...")
    
    else:

        print("companies_all_statistics document error...")




    
    
                

        


