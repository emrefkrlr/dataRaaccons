from django.shortcuts import render, redirect
from authentication.service import UserService, Authantication
from layout.layout_service import LayoutService
from activities.service import ActivitiesService
from products.service import ProductsService, ProductMatchesService
from mongo.services import MongoService
from companies.service import CompaniesService

# Create your views here.


def activity_categorry_list(request, activity):

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
            context["user_info"] = user_info
            context["p_recent_main_menu"] = "Products"
            context["p_recent_sub_menu"] = activity.name
            context["package_type"] = user_info["package_type"]
            context["activity_categories"] = ActivitiesService().get_activity_categories(activity=activity)

            page = render(request, 'raccoon_analytic/pages/activity_category_list.html', context)

        else:

            # Expire Olmuş sayfa tasarla
            page = redirect('index')
           
        response = page
       
    else:
        response = redirect('index')

    return response


def product_lists(request, activity_category):

    auth_user = request.user.id
    activity_category = ActivitiesService().get_activity_category_by_name(activity_category=activity_category)
    context = {
        "title": "{} | RaccoonAnalytic Your smart assistant with data solutions.".format(activity_category)
    }

    if auth_user:

        user_info = UserService().get_user(auth_user)

        if user_info["dashboard_status"]:

            menues = LayoutService().get_menues(auth_user)
            context["menues"] = menues
            context["user_info"] = user_info
            context["p_recent_main_menu"] = "Products"
            context["p_recent_sub_menu"] = activity_category
            context["package_type"] = user_info["package_type"]
            context["product_lists"] = ProductsService().get_products({"activity_category":activity_category})
            sub_categories = ProductsService().get_unique_sub_categories_by_filter(**{"activity_category": activity_category})
            context["sub_category_filter"] = sub_categories
            context["company_filter"] = []
            companies = ProductsService().get_companies_by_activity_category(activity_category=activity_category)
            for company_id in companies:
                company = CompaniesService().get_company_by_id(company=company_id["company"])
                context["company_filter"].append(company.name)

            page = render(request, 'raccoon_analytic/pages/product_lists.html', context)

        else:

            # Expire Olmuş sayfa tasarla
            page = redirect('index')
           
        response = page
       
    else:
        response = redirect('index')

    return response




def product_deatil(request, id):


    auth_user = request.user.id
    product = ProductsService().get_product_by_id(id=id)
    activity = ActivitiesService().get_activity(activity=product.activity)
    activity_category = ActivitiesService().get_activity_category_by_name(activity_category=product.activity_category)
    activity_category_sub_name = ActivitiesService().get_activity_sub_category_by_name(activity=activity, activity_category=activity_category, activity_sub_category=product.activity_sub_category)
    

    context = {
        "title": "{} | RaccoonAnalytic Your smart assistant with data solutions.".format(product.product_name)
    }

    if auth_user:

        user_info = UserService().get_user(auth_user)

        if user_info["dashboard_status"]:
    
            menues = LayoutService().get_menues(auth_user)
            context["menues"] = menues
            context["user_info"] = user_info
            context["p_recent_main_menu"] = "Products"
            context["p_recent_sub_menu"] = product.product_name
            context["package_type"] = user_info["package_type"]
            context["product"] = product
            context["activity_category_name"] = activity_category.name
            context["activity_sub_category_name"] = str(activity_category_sub_name)

            # PRODUCT STATISTICS
            activity_sub_category_avg_price = ProductsService().get_activity_sub_category_descriptive_statistics(activity=activity, activity_category=activity_category, activity_sub_category=activity_category_sub_name)
            
            context["activity_category_detail"] = {
                "price__avg": round(activity_sub_category_avg_price["price__avg"], 3) if activity_sub_category_avg_price["price__avg"] else 0,
                "price__min": round(activity_sub_category_avg_price["price__min"], 3) if activity_sub_category_avg_price["price__min"] else 0,
                "price__max": round(activity_sub_category_avg_price["price__max"], 3) if activity_sub_category_avg_price["price__max"] else 0,
                "price__count": round(activity_sub_category_avg_price["price__count"], 3) if activity_sub_category_avg_price["price__count"] else 0,
            }

            # MATCHES PRODUCTS

            matches_products = ProductMatchesService().get_product_matches_products(id=product.id)
            if matches_products:
                matches_products.sort(key=lambda x: x.price, reverse=True)
            
            if matches_products:
                context["matches_products"] = matches_products

            page = render(request, 'raccoon_analytic/pages/product_detail.html', context)

        else:

            # Expire Olmuş sayfa tasarla
            page = redirect('index')
           
        response = page
       
    else:
        response = redirect('index')

    return response