from django.shortcuts import render,redirect
from dashboard.service import DashboardService
from authentication.service import UserService, Authantication
from layout.layout_service import LayoutService
from activities.service import ActivitiesService

# Create your views here.

def activity_overview_dashboard(request, activity):
    
    auth_user = request.user.id
    activity = ActivitiesService().get_activity(activity=activity)
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
            context["package_type"] = user_info["package_type"]
            context["recent_sub_menu"] = activity.name
            
            context["general_statistics"] = DashboardService().get_general_statistics(activity=activity)
            context["companies_statistics"] = DashboardService().get_companies_statistics(activity=activity)

            if user_info["company"]:
                
                main_company = user_info["company"]
                context["main_company_statistics"] = DashboardService().get_main_company_statistics(activity=activity, main_company=main_company)
                    
            page = render(request, 'raccoon_analytic/pages/activity_dashboard.html', context)

        else:
            # Expire Olmuş sayfa tasarla
            page = redirect('index')
        
        response = page
        
    else:

        response = redirect('index')
            
    return response


def activity_category_dashboard(request, activity, activity_category):

    # check_product_count = ProductsService().count_of_products_by_filter({'status': 1})

    auth_user = request.user.id
    activity = ActivitiesService().get_activity(activity=activity)
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
            context["package_type"] = user_info["package_type"]
            context["recent_sub_menu"] = activity_category
            
            context["general_statistics"] = DashboardService().get_general_statistics(activity=activity, activity_category=activity_category)
            context["companies_statistics"] = DashboardService().get_companies_statistics(activity=activity, activity_category=activity_category)
           
            if user_info["company"]:
                
                main_company = user_info["company"]
                context["main_company_statistics"] = DashboardService().get_main_company_statistics(main_company=main_company, activity=activity, activity_category=activity_category)
               
            page = render(request, 'raccoon_analytic/pages/activity_dashboard.html', context)

        else:
            # Expire Olmuş sayfa tasarla
            print("Expire olmuş..{}".format(auth_user))
            page = redirect('index')
        
        response = page
        
    else:

        response = redirect('index')
            
    return response

        