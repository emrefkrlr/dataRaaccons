from django.shortcuts import render
from layout.layout_service import LayoutService
from package.service import PackageService
from products.service import ProductsService
from companies.service import CompaniesService


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

    if user:
        
        context['dashboard_url'] = True
        menu = LayoutService().get_menues(user)
        context['menu'] = menu[0]["menu"][0]["main_menu"]

    response = render(request, 'raccoon_analytic/pages/index.html', context)

    return response
