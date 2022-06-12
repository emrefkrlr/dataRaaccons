from products.service import ProductsService
from companies.service import CompaniesService
from activities.service import ActivitiesService
from mongo.services import MongoService
from statistics import mean


class DashboardService(object):


### MAIN COMPANY STATISTICS ###

    def main_company_activity_category_based_statistics(self, company_id, activity_id):
        
        try:
            results = []

            company_info = {

                "company_name": CompaniesService().get_company(company_id=company_id).name,
                "company_logo": "http://asdasgasdgasdgasd.img",
                "dashboard_data": []
            }

            activity_categories = ActivitiesService().get_activity_categories(activity_id=activity_id)
                
            for activity_category in activity_categories:
                dashboard_data = {
                    "activity_category": activity_category.name,
                    "count_sub_category": len(ProductsService().get_unique_sub_categories_by_filter(**{'status': 1, 'company': company_id, 'activity': activity_id, 'activity_category': activity_category.id })),
                    "count_product": ProductsService().count_of_products_by_filter(**{'status': 1, 'company': company_id, 'activity': activity_id, 'activity_category': activity_category.id })
                }
                
                company_info["dashboard_data"].append(dashboard_data)
                    
            results.append(company_info)

            return results
        
        except Exception as e:
            print("\n DashboardService main_company_activity_category_based_statistics Exeption: \n{}".format(e))


    def main_company_activity_category_based_products_ratio(self, company_id, activity_id):

        try:

            results = []

            company_info = {

                "company_name": CompaniesService().get_company(company_id=company_id).name,
                "company_logo": "http://asdasgasdgasdgasd.img",
                "dashboard_data": []
            }

            activity_categories = ActivitiesService().get_activity_categories(activity_id=activity_id)
            company_all_product_count = ProductsService().count_of_products_by_filter(**{'status': 1, 'company': company_id, 'activity': activity_id})
            
            for activity_category in activity_categories:
                activity_category_count = ProductsService().count_of_products_by_filter(**{'status': 1, 'company': company_id, 'activity': activity_id, 'activity_category': activity_category.id })
                dashboard_data = {
                    "activity_category": activity_category.name,
                    "count_sub_category": len(ProductsService().get_unique_sub_categories_by_filter(**{'status': 1, 'company': company_id, 'activity': activity_id, 'activity_category': activity_category.id })),
                    "products_ratio": round((activity_category_count/company_all_product_count)*100, 3)
                }
                
                company_info["dashboard_data"].append(dashboard_data)
                    
            results.append(company_info)

            return results
        
        except Exception as e:
            print("\n DashboardService main_company_activity_category_based_products_ratio Exeption: \n{}".format(e))


    def main_company_sub_category_based_products_price(self, company_id, activity_id, activity_category_id, activity_category_name):

        try:
            results = []

            sub_categories = ProductsService().get_unique_sub_categories_by_filter({**{'status': 1, 'company': company_id, 'activity': activity_id, 'activity_category': activity_category_id }})
            for sub_category in sub_categories:

                dashboard_data = {
                    "activity_category": activity_category_name,
                    "sub_category": sub_category["sub_category"],
                    "product_count": ProductsService().count_of_products_by_filter(**{'status': 1, 'company': company_id, 'activity': activity_id, 'activity_category': activity_category_id }),
                    "avg_price": 0,
                    "max_price": 0,
                    "min_price": 0
                    }

                price = []

                documents = MongoService().get_sub_category_price(db_name='DataRaccoons', 
                host='dataRaccoonsMongo', port='27017', username='root', 
                password='root', collection='market', query={"info.company_name": "getir_getir", "info.activity_category": str(activity_category_name)})

                for document in documents:
            
                    if document is not None and document["products_and_price"] is not None and len(document["products_and_price"]) > 0 :
                        __DOC = True
                        for product_and_price in document["products_and_price"]:
                            
                            if sub_category["sub_category"] == product_and_price["sub_category"]:
                                price.append(round(float(product_and_price["price"])))

                    dashboard_data["avg_price"] = round(mean(price),3)
                    dashboard_data["max_price"] = round(max(price),3)
                    dashboard_data["min_price"] = round(min(price),3)
                
                    if __DOC:
                        break

                results.append(dashboard_data)	

            return results

        except Exception as e:
            print("\n DashboardService main_company_activity_category_based_products_price Exeption: \n{}".format(e))


### ALL COMPANY CORSS STATISTICS ###

    def activity_category_based_product_statistics_of_companies(self, main_company_id = None, activity_id = None):

        try:

            results = []
            
            companies = CompaniesService().get_companies()
            
            for company in companies:
                
                company_info = {
                    "main_company": 1 if company.id == main_company_id else 0,
                    "company_name": company.name,
                    "company_logo": "http://asdasgasdgasdgasd.img",
                    "dashboard_data": []
                }
                
                activity_categories = ActivitiesService().get_activity_categories(activity_id=activity_id)
                
                for activity_category in activity_categories:
                    
                    dashboard_data = {
                        "activity_category": activity_category.name,
                        "count_sub_category": len(ProductsService().get_unique_sub_categories_by_filter(**{'status': 1, 'company': company.id, 'activity': activity_id, 'activity_category': activity_category.id })),
                        "count_product": ProductsService().count_of_products_by_filter(**{'status': 1, 'company': company.id, 'activity': activity_id, 'activity_category': activity_category.id })
                    }
                    company_info["dashboard_data"].append(dashboard_data)
                    
                results.append(company_info)
            
            return results
        
        except Exception as e:
            print("\n activity_category_based_product_statistics_of_companies Exeption: \n{}".format(e))

    
    def activity_category_based_products_ratio_of_companies(self, main_company_id = None, activity_id = None):

        try:
            
            results = []
            
            companies = CompaniesService().get_companies()
            
            for company in companies:
                
                company_info = {
                    "main_company": 1 if company.id == main_company_id else 0,
                    "company_name": company.name,
                    "company_logo": "http://asdasgasdgasdgasd.img",
                    "dashboard_data": []
                }
                
                activity_categories = ActivitiesService().get_activity_categories(activity_id=activity_id)
                company_all_product_count = ProductsService().count_of_products_by_filter(**{'status': 1, 'activity': activity_id})

                for activity_category in activity_categories:
                    activity_category_count = ProductsService().count_of_products_by_filter(**{'status': 1, 'company': company.id, 'activity': activity_id, 'activity_category': activity_category.id })
                    dashboard_data = {
                        "activity_category": activity_category.name,
                        "count_sub_category": len(ProductsService().get_unique_sub_categories_by_filter(**{'status': 1, 'company': company.id, 'activity': activity_id, 'activity_category': activity_category.id })),
                        "products_ratio": round((activity_category_count/company_all_product_count)*100,3)
                        
                    }
                    company_info["dashboard_data"].append(dashboard_data)
                    
                results.append(company_info)
            
            return results

        except Exception as e:
            print("\n DashboardService activity_category_based_products_ratio_of_companies Exeption: \n{}".format(e))