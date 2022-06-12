from companies.models import Companies, CompanyActivities


class CompaniesService(object):

    def get_companies(self):

        try:
            results = Companies.objects.filter(**{'status': 1})

            return results

        except Exception as e:
            print("\nget_companies Exeption: \n{}".format(e))


    def get_company(self, company_id):

        try:
            results = Companies.objects.get(pk=company_id)

            return results

        except Exception as e:
            print("\nget_companies Exeption: \n{}".format(e))