import email
from multiprocessing import context
from django.shortcuts import render, redirect
from account.services import AccountService
from authentication.service import UserService, Authantication
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from layout.layout_service import LayoutService
import time
from vendor.email.email import send_mail, templates
from django.conf import settings

# Create your views here.

def login(request, verified_code = None):

    # İlk confirmeden sonra kullanıcının deneme süresi 
    # başlar accountda expire dateyi set et ve dashboarddaki notificationada gönder.
    context = {}

    if verified_code:

        verified_user = UserService().user_comfirmed(verified_code=verified_code)

        if verified_user is False:
            context['error_message'] = "Your account is not verified contact your administrator."

    if request.POST:

        user = UserService().login_user(email = request.POST['email'], password = request.POST['password'])

        if user[0]:
            
            auth_login(request, user[1])
            menu = LayoutService().get_menues(user[1])
            Authantication.getInstance().setUser(user[1].id)
            #response.set_cookie('username', user[1].username)
            response = redirect('dashboard:activity', menu[0]["menu"][0]["main_menu"])
            
            return response
        
        else:
            context['error_message'] = user[1]

    response = render(request, 'raccoon_analytic/pages/login.html', context=context)

    return response



def create_account(request, package=None):

    confirmed_url = "{}/auth/login/".format(request.META["HTTP_HOST"])

    context = {}
    if request.POST:
        
        user = UserService().set_new_user(
            username = request.POST['username'],
            email = request.POST['email'],
            password = request.POST['password'], 
            confirmed_url = confirmed_url
            )

        if user[0]:
            response = redirect('index')
            time.sleep(5)
            return response
        else:
            context['error_message'] = user[1]
    
    response = render(request, 'raccoon_analytic/pages/create_account.html', context=context)

    return response


def logout(request):
    

    if UserService().logout_user(request.user):

        auth_logout(request)
        response = redirect('authentication:login')
        return response
    
    else:
        print("Burada hata var incele...",)


def reset_password(request):

    if request.POST:
        user = UserService().get_user_by_email(request.POST['email'])
        account = AccountService().get_user_account(user=user)
        confirmed_url = "{}/auth/new_password/".format(request.META["HTTP_HOST"])
        confirmed_url = confirmed_url + account.verified_code
        
        send_mail(subject="Reset Password",from_address=settings.EMAIL_HOST_USER, to_address=request.POST['email'], template="raccoon_analytic/email/password-reset.html", confirm_code=confirmed_url)
    
    response = render(request, 'raccoon_analytic/pages/password_reset.html')

    return response


def set_new_password(request, token):

    if request.POST:
        
        UserService().update_user_password(token=token, password=request.POST['password'])

    context = {
        "token": token
    }
    response = render(request, 'raccoon_analytic/pages/new_password.html', context)
    return response

    

