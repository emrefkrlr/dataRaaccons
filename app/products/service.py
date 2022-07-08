from products.models import Products, ProductMatches
from datetime import datetime, timedelta


class ProductsService(object):

    def get_products(self, filter):
        
        try:
            if bool(filter):
                results = Products.objects.filter(**filter)
                return results
                
            else:
                raise Exception('dictionary is null')
        
        except Exception as e:
            print("\nget_products Exeption: \n{}".format(e))


    def exclude(self, id):

        try:
            result = Products.objects.exclude(id=id)

            return result

        except Exception as e:
            print("\nexclude Exeption: \n{}".format(e))

    def insert_new_products(self, **params):
        
        try:
            insert = Products.objects.get_or_create(**params)
            
            if insert:
                return True
            else:
                raise Exception('insert failed.')

        except Exception as e:
            print("\ninsert_new_products Exeption: \n{}".format(e))


    def insert_product_matches(self, **params):

        try:
            insert = ProductMatches.objects.get_or_create(**params)
            
            if insert:
                return True
            else:
                raise Exception('insert failed.')

        except Exception as e:
            print("\ninsert_product_matches Exeption: \n{}".format(e))


    def get_unique_sub_categories_by_filter(self, year=False, month=False, week=False, **filter):
        
        try:
            if [year,month, week].count(True) == 1:
                
                current_date = datetime.now()
                
                if year:
                    
                    previous_date = current_date - timedelta(days= 365)
                    
                elif month:
                    
                    previous_date = current_date - timedelta(days= 30)
                    
                else:
                    
                    previous_date = current_date - timedelta(days= 7)

                results = Products.objects.filter(created_at__range = (current_date, previous_date), **filter).distinct('sub_category').values("sub_category")
            
            else:

                results = results = Products.objects.filter(**filter).distinct('sub_category').values("sub_category")
            
            return results if results else False
           
                
        except Exception as e:
            print("\nget_unique_sub_categories Exeption: \n{}".format(e))


    def get_companies(self, activity, activity_category=None):

        try:

            if activity_category:
                
                companies = Products.objects.filter(activity=activity, activity_category=activity_category).distinct("company").values("company")
            
            else:
                companies = Products.objects.filter(activity=activity).distinct("company").values("company")

            return companies if companies else False
        
        except Exception as e:

            print("ProductService get_companies_in_activity Exception: {} Activity: {}".format(e, activity))


    def count_of_products_by_filter(self, year=False, month=False, week=False, **filter,):

        try:
            
            if [year,month, week].count(True) == 1:
                
                current_date = datetime.now()
                
                if year:
                    
                    previous_date = current_date - timedelta(days= 365)
                    
                elif month:
                    
                    previous_date = current_date - timedelta(days= 30)
                    
                else:
                    
                    previous_date = current_date - timedelta(days= 7)
               

                results = Products.objects.filter(created_at__range = (current_date, previous_date), **filter).count()

            else:
                
                results = Products.objects.filter(**filter).count()

            return results if results else 0
                
        except Exception as e:
            print("\ncount_of_products_by_filter Exeption: \n{}".format(e))


    


    def get_last_update_at(self, activity):

        last_update = Products.objects.filter(status=1, activity=activity).order_by("-id").first()
        print(last_update)

        return last_update.updated_at


    
    