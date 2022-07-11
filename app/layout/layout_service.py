from account.services import AccountService
from activities.service import ActivitiesService
from companies.service import CompaniesService

class LayoutService(object):


    def get_menues(self, user):

        try:

            account_company = AccountService().get_user_company(user=user)
            menues = [{
                "menu": [],
                "products": []
            }]

            if account_company:

                main_menues = CompaniesService().get_company_activities(company = account_company.company)
                
                for main_menu in main_menues:
                    
                    sub_menues = ActivitiesService().get_activity_categories(main_menu.activity)

                    data = {
                        "main_menu": main_menu.activity,
                        "sub_menues": sub_menues
                    }

                    menues[0]["menu"].append(data)
                    menues[0]["products"].append({"products_activity": main_menu.activity})
                    


            else:
                main_menues = ActivitiesService().get_personal_activities()

                for main_menu in main_menues:

                    sub_menues = ActivitiesService().get_activity_categories(main_menu)

                    data = {
                        "main_menu": main_menu,
                        "sub_menues": sub_menues
                    }

                    menues[0]["menu"].append(data)
                    menues[0]["products"].append({"products_activity": main_menu.activity})

            
                    
            return menues
        
        except Exception as e:
            print(" LayoutService get_menues Exception: {}".format(e))