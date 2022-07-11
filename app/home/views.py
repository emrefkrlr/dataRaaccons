from django.shortcuts import render
from authentication.service import UserService, Authantication
from layout.layout_service import LayoutService

# Create your views here.

def index(request):

    context = {
        'dashboard_url': False
    }

    user = Authantication.getInstance().getUser()
    if user:
        context['dashboard_url'] = True
        menu = LayoutService().get_menues(user)
        context['menu'] = menu[0]["menu"][0]["main_menu"]

    response = render(request, 'raccoon_analytic/pages/index.html', context)

    return response
