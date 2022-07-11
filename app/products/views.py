from django.shortcuts import render, redirect
from authentication.service import UserService, Authantication
from layout.layout_service import LayoutService
from activities.service import ActivitiesService
from products.service import ProductsService, ProductMatchesService
from mongo.services import MongoService
from companies.service import CompaniesService

# Create your views here.


def activity_categorry_list(request, activity):

    auth_user = Authantication.getInstance().getUser()
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

    auth_user = Authantication.getInstance().getUser()
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


            print("\n\n\n-------------------------------> ", context["sub_category_filter"])
            print("\n\n\n-------------------------------> ", context["company_filter"])



            page = render(request, 'raccoon_analytic/pages/product_lists.html', context)

        else:

            # Expire Olmuş sayfa tasarla
            page = redirect('index')
           
        response = page
       
    else:
        response = redirect('index')

    return response




def product_deatil(request, id):


    auth_user = Authantication.getInstance().getUser()
    product = ProductsService().get_product_by_id(id=id)
    activity = ActivitiesService().get_activity(activity=product.activity)
    activity_category = ActivitiesService().get_activity_category_by_name(activity_category=product.activity_category)

    
    

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

            # PRODUCT STATISTICS
            mongo_query = MongoService().avg_price_query_generator(get_id="sub_category", activity=activity, activity_category=activity_category, sub_category=product.sub_category)

            activity_category_product_statistics_data = MongoService().get_avg_data(collection=activity, query=mongo_query)

            if len(activity_category_product_statistics_data) > 0:
                
                activity_category_detail = {
                    "product_count": activity_category_product_statistics_data[0]["count"],
                    "min_price": round(min(activity_category_product_statistics_data[0]["minPrice"]), 3) if type(activity_category_product_statistics_data[0]["minPrice"]) == list else activity_category_product_statistics_data[0]["minPrice"],
                    "max_price": round(max(activity_category_product_statistics_data[0]["maxPrice"]), 3) if type(activity_category_product_statistics_data[0]["maxPrice"]) == list else activity_category_product_statistics_data[0]["maxPrice"],
                    "avg_price": round(activity_category_product_statistics_data[0]["averagePrice"], 3) if activity_category_product_statistics_data[0]["averagePrice"] else None,
                }

            else:

                activity_category_detail = {
                    "product_count": 0,
                    "min_price": 0,
                    "max_price": 0,
                    "avg_price": 0,
                }

            context["activity_category_detail"] = activity_category_detail


            # MATCHES PRODUCTS

            matches_products = ProductMatchesService().get_product_matches_products(id=product.id)

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