from django.shortcuts import render
from authentication.service import UserService, Authantication
from layout.layout_service import LayoutService
from package.service import PackageService
from products.service import ProductsService
from companies.service import CompaniesService
from products.models import Products, ProductMatches
from mongo.services import MongoService
from products.tasks import insert_new_products_task, product_matches_task
from dashboard.tasks import activity_based_descriptive_statistics, activity_category_based_descriptive_statistics, company_based_activity_category_descriptive_statistics, company_based_activity_sub_category_descriptive_statistics, companies_all_statistics,dashbord_descriptive_statistics_task

# Create your views here.

def index(request):

    context = {
        'dashboard_url': False
    }

    user = request.user.id
    context['packages'] = PackageService().get_all_packages()
    context['product_count'] = ProductsService().count_of_products_by_filter({'status': 1})
    context['company_count'] = CompaniesService().get_all_companies()
    context['sub_category_count'] = ProductsService().get_unique_sub_categories_by_filter({'status': 1})


    ProductMatches.objects.all().delete()
    Products.objects.all().delete()
    #insert_new_products_task()
    #product_matches_task()
    

    #print(MongoService().delete_collection("market"))

    
    #dashbord_descriptive_statistics_task()
    #activity_based_descriptive_statistics()
    #activity_category_based_descriptive_statistics()
    #company_based_activity_category_descriptive_statistics()
    #company_based_activity_sub_category_descriptive_statistics()
    #companies_all_statistics()



    if user:
        
        context['dashboard_url'] = True
        menu = LayoutService().get_menues(user)
        context['menu'] = menu[0]["menu"][0]["main_menu"]

    response = render(request, 'raccoon_analytic/pages/index.html', context)

    return response
