from django.shortcuts import render,redirect
from dashboard.service import DashboardService
from authentication.service import UserService, Authantication
from layout.layout_service import LayoutService
from activities.service import ActivitiesService
from datetime import datetime, timedelta
from mongo.services import MongoService


# Create your views here.

def dashboard(request, activity, activity_category=None):

    auth_user = Authantication.getInstance().getUser()
    activity = ActivitiesService().get_activity(activity=activity)
    model_activity_category = ActivitiesService().get_activity_categories(activity=activity)

    context = {
        "title": "{} | RaccoonAnalytic Your smart assistant with data solutions.".format(activity.name)
    }

    if auth_user:

        user_info = UserService().get_user(auth_user)

        if user_info["dashboard_status"]:

            menues = LayoutService().get_menues(auth_user)
            context["menues"] = menues
            context["last_update"] = DashboardService().get_last_update_activity_date(activity=activity)
            context["user_info"] = user_info
            context["recent_main_menu"] = activity.name


            if activity_category:

                if user_info["company"]:

                    main_company = user_info["company"]

                    context["comparative_statistics_on_activity_for_the_main_company"] = DashboardService().comparative_statistics_on_activity_for_the_main_company(activity=activity, activity_category=activity_category, main_company=main_company)
                    context["category_based_statistics_of_companies_for_activities"] = DashboardService().category_based_statistics_of_companies_for_activities(activity=activity, activity_category=activity_category, main_company=main_company)
                
                else:

                    context["category_based_statistics_of_companies_for_activities"] = DashboardService().category_based_statistics_of_companies_for_activities(activity=activity, activity_category=activity_category)
                
                context["recent_sub_menu"] = activity_category
                context["price_information_of_the_activities"] = DashboardService().price_information_of_the_activities(activity=activity, activity_category=activity_category)
                context["all_comparative_statistics_data_for_activities"] = DashboardService().all_comparative_statistics_data_for_activities(activity=activity, activity_category=activity_category)
                context["number_of_products_for_activities"] = DashboardService().number_of_products_for_activities(activity=activity, activity_category=activity_category)
                context["number_of_companies_for_activities"] = DashboardService().number_of_companies_for_activities(activity=activity, activity_category=activity_category)
                context["product_distribution_of_companies_in_activities"] = DashboardService().product_distribution_of_companies_in_activities(activity=activity, activity_category=activity_category)
                

                page = render(request, 'raccoon_analytic/pages/activity_dashboard.html', context)

            else:
                
                if user_info["company"]:

                    main_company = user_info["company"]

                    context["comparative_statistics_on_activity_for_the_main_company"] = DashboardService().comparative_statistics_on_activity_for_the_main_company(activity=activity, main_company=main_company)
                    context["category_based_statistics_of_companies_for_activities"] = DashboardService().category_based_statistics_of_companies_for_activities(activity=activity, main_company=main_company)
                
                else:
                
                    context["category_based_statistics_of_companies_for_activities"] = DashboardService().category_based_statistics_of_companies_for_activities(activity=activity)
                
                context["recent_sub_menu"] = activity.name
                context["price_information_of_the_activities"] = DashboardService().price_information_of_the_activities(activity=activity)
                context["all_comparative_statistics_data_for_activities"] = DashboardService().all_comparative_statistics_data_for_activities(activity=activity, activity_category=activity_category)
                context["number_of_products_for_activities"] = DashboardService().number_of_products_for_activities(activity=activity)
                context["number_of_companies_for_activities"] = DashboardService().number_of_companies_for_activities(activity=activity)
                context["product_distribution_of_companies_in_activities"] = DashboardService().product_distribution_of_companies_in_activities(activity=activity)
                
                page = render(request, 'raccoon_analytic/pages/activity_dashboard.html', context)

        else:

            # Expire Olmuş sayfa tasarla
            page = redirect('index')
           
       
        response = page
       
    else:
        response = redirect('index')

    return response
