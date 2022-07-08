from shutil import ExecError
from account.models import Account, UserType, AccountCompany


class AccountService(object):


    def get_user_account(self, user):

        try:

            account = Account.objects.get(user = user)

            return account if account else False

        except Exception as e:
            print("AccountService get_user_account Exception: {} \n User: {}".format(e, user))


    def set_user_account(self, user, **kwargs):

        try:

            account = Account.objects.update_or_create(user=user, **kwargs)

            return account if account else False

        except Exception as e:
            print("AccountService set_user_account Exception: {} \n User: {}".format(e, user))


    def update_user_account(self, user, **kwargs):

        try:
            
            account = Account.objects.filter(user=user).update(**kwargs)

            return account if account else False
        
        except Exception as e:
            print("AccountService update_user_account Exception: {} \n User: {}".format(e, user))


    def get_user_type(self, user_type):

        try:

            user_type = UserType.objects.get(name=user_type)

            return user_type if user_type else False

        except Exception as e:
            print("AccountService get_user_type Exception: {}".format(e))

    def get_user_type_personal(self):

        try:
            
            user_type = UserType.objects.get(name="personal")

            return user_type if user_type else False
        
        except Exception as e:
            print("AccountService get_user_type_personal Exception: {}".format(e))


    def get_user_type_corporate(self):

        try:

            user_type = UserType.objects.get(name="corporate")

            return user_type if user_type else False

        except Exception as e:
            print("AccountService get_user_type_corporate Exception: {}".format(e))


    def get_user_company(self, user):

        try:

            account_company = AccountCompany.objects.filter(user=user)
            
            if len(account_company)>0:
                account_company = account_company[0]

            # return user company first element
            return account_company if account_company else False

        except Exception as e:
            print("AccountService get_user_company Exception: {} \n User: {}".format(e, user))

