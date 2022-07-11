from importlib.resources import Package
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from account.services import AccountService
from package.service import PackageService
from companies.service import CompaniesService
from activities.service import ActivitiesService
from vendor.email.email import send_mail, templates
import uuid


class Authantication(object):
    __instance = None
    _user = None

    @staticmethod
    def getInstance():
        
        if Authantication.__instance == None:
            Authantication()
        return Authantication.__instance


    def setUser(self, user):
        u = Authantication.getInstance()
        u._user = user


    def getUser(self):
        u = Authantication.getInstance()
        return u._user


    def __init__(self):
        if Authantication.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Authantication.__instance = self


    def logutInstance(self):
        Authantication.__instance = None
        Authantication._user = None


class UserService(object):

    def set_new_user(self, *args, **kwargs):

        error_message = []
        confirme_code = str(uuid.uuid4().hex)
        email =  User.objects.filter(email=kwargs['email'])
        username = User.objects.filter(username=kwargs['username'])
        
        if email or username:
            error_message.append("Using email or username. If you don't remember your password, you can reset your password") 
            return False, error_message
            
        else:
            user = User.objects.create_user(username=kwargs["username"], email=kwargs["email"])
            user.set_password(kwargs["password"])
            user.save()

            user_type = AccountService().get_user_type_personal()
        
            AccountService().set_user_account(user=user, verified_code=confirme_code, verified=0, user_type=user_type)

            free_trial_package = PackageService().get_package("Free Trial")
            PackageService().set_user_package(user, free_trial_package)

            confirmed_url = kwargs["confirmed_url"] + confirme_code
        
            #send_mail(mail_address=[kwargs["email"]], template="raccoon_analytic/email/verify_email.html", confirm_code=confirmed_url)
            
            return True, user


    def login_user(self, **kwargs):

        
        error_message = []
        user =  User.objects.get(email=kwargs['email'])

        if user:

            auth_user = authenticate(username = str(user.username), password = str(kwargs["password"]))
            AccountService().update_user_account(user, is_online=1)
            
            if auth_user:
                return True, auth_user
            
            else:
                error_message.append("Oops! Email or password looks wrong.")
                return False, error_message
        
        else:
            error_message.append("We could not find such a user. If you remember being a member, I suggest resetting your password.")
            return False, error_message


    def logout_user(self, user):
        
        account = AccountService().update_user_account(user=user, is_online=0)

        return account if account else False
        
        
    def get_user(self, user):

        user = User.objects.get(pk=user)

        if user:

            account = AccountService().get_user_account(user=user)
            account_company = AccountService().get_user_company(user=user)
            if account_company:
                company = CompaniesService().get_company_by_name(company=account_company.company)
            else:
                company = False

            package_warning = PackageService().get_user_package_warning(user=user)


            user_info = {

                "username": user.username,
                "email": user.email,
                "first_name": user.first_name if user.first_name else None,
                "last_name": user.last_name if user.last_name else None,
                "user_type_id": AccountService().get_user_type(account.user_type).id,
                "user_type": account.user_type,
                "profile": account.profile if account.profile else None,
                "package_type": package_warning[2],
                "package_message": package_warning[1] if package_warning[1] else None,
                "dashboard_status": package_warning[0],
                "company": company.name if company else None,
                "company_id": company.id if company else None,
            }
        
            return user_info

        else:
            return False


        
            


            
            
        
        
        

