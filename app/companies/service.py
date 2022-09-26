from unicodedata import name
from companies.models import Companies, CompanyActivities


class CompaniesService(object):


    def get_all_companies(self):

        try:

            results = Companies.objects.filter(status = 1)

            return results if results else False

        except Exception as e:
            print("CompaniesService get_all_companies Exeption: {}".format(e))


    def get_company_by_name(self, company):

        try:

            results = Companies.objects.get(name=company, status=1)

            return results if results else False

        except Exception as e:
            print("CompaniesService get_company_by_name Exeption: {} \n Company: {}".format(e, company))


    def get_company_by_id(self, company):

        try:

            results = Companies.objects.get(pk=int(company), status=1)

            return results if results else False

        except Exception as e:
            print("CompaniesService get_company_by_id Exeption: {} \n Company: {}".format(e, company))


        


    def get_company_activities(self, company):

        try:

            activities = CompanyActivities.objects.filter(company=company)

            return activities if activities else False

        except Exception as e:
            print("CompaniesService get_company_activities Exception: {} \n Company: {}".format(e,company))

    
    def get_companies_by_activity(self, activity):

        try:

            companies = CompanyActivities.objects.filter(activity=activity)

            return companies if companies else False
        
        except Exception as e:
            print(" CompaniesService get_companies_by_activity Exception: {} \n Company {}".format(e,activity))