from products.models import Products, ProductMatches


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


    def get_unique_sub_categories_by_filter(self, **filter):
        
        try:
            if bool(filter):
                results = Products.objects.filter(**filter).distinct('sub_category').values("sub_category")
                return results
            else:
                raise Exception('dictionary is null')
                
        except Exception as e:
            print("\nget_unique_sub_categories Exeption: \n{}".format(e))


    def count_of_products_by_filter(self, **filter):

        try:
            if bool(filter):
                results = Products.objects.filter(**filter).count()
                return results
            else:
                raise Exception('dictionary is null')
                
        except Exception as e:
            print("\ncount_of_products_by_filter Exeption: \n{}".format(e))
    