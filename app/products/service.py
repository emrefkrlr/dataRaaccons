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

    
    def get_product_by_id(self, id):

        try:

            results = Products.objects.get(pk=id)

            return results if results else False

        except Exception as e:
            print("get_product_by_id Exeption: \n{}".format(e))


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

    def update_or_create_products(self, **params):

        try:

            update_or_create = Products.objects.update_or_create(**params)

            return update_or_create if update_or_create else False

        except Exception as e:
            print("update_or_create_products Exeption: \n{}".format(e))


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



    def get_companies_by_activity_category(self, activity_category):

        try:
    
            companies = Products.objects.filter(activity_category=activity_category).distinct("company").values("company")
           

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
        

        return last_update.updated_at

    
class ProductMatchesService(ProductsService):

    def get_product_matches_products(self, id):
        
        try:
            
            matched_poducts = ProductMatches.objects.filter(first_product_id=id)

            produts = []

            for product in matched_poducts:

                product = self.get_product_by_id(id=product.second_product_id)

                produts.append(product)

            return produts if len(produts) > 0 else False

        except Exception as e:
            print("get_product_matches_products Exeption: \n{}".format(e))
