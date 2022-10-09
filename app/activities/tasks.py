from __future__ import absolute_import, unicode_literals
from asyncio.log import logger
from celery import shared_task
from activities.service import ActivitiesService
from products.service import ProductsService

@shared_task
def insert_new_sub_category():

    print("Celery insert_new_sub_category started....")

    activities = ActivitiesService().get_all_activities()

    for activity in activities:

        product_sub_categories = ProductsService().get_unique_sub_categories_by_filter({"activity": activity})

        mapping_sub_categories = ActivitiesService().get_mapping_activity_sub_categories_by_activity(activity=activity).values_list("mongo_sub_category", flat=True)

        for product_sub_category in product_sub_categories:

            if product_sub_category["sub_category"] not in mapping_sub_categories:

                ActivitiesService().insert_sub_category(
                    mapping_activity = activity,
                    mapping_activity_category = ActivitiesService().get_activity_category_by_name(activity_category="Meyve ve Sebze"),
                    mapping_activity_sub_category = ActivitiesService().get_activity_sub_category_by_name(activity_sub_category="Kontrol"),
                    mongo_sub_category = product_sub_category["sub_category"]
                )
    
    print("Celery insert_new_sub_category done....")