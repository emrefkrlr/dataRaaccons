from crawlers.scraper import *
from crawlers import functions
import uuid
import json

class IsteGelsinCrawler(object):

    def get_innerHTML(self, url, page=None):

        post_body_data = json.dumps({"query":"\nquery CatalogSearch2(\n  $addressId: String\n  $lat: Float\n  $lon: Float\n  $size: Int\n  $from: Int\n  $sortingAscending: Boolean\n  $sortingType: String\n  $categories: [String]\n  $orCategories: [String]\n  $brands: [String]\n  $orBrands: [String]\n  $groups: [String]\n  $orGroups: [String]\n  $filters: [String]\n  $tags: [String]\n  $orTags: [String]\n  $withAllCategories: Boolean\n  $withAllSubCategories: Boolean\n  $withAllBrands: Boolean\n  $withOnlyGivenCategory: Boolean\n  $inStock: Boolean\n) {\n  catalogSearch2(\n    addressId: $addressId\n    lat: $lat\n    lon: $lon\n    size: $size\n    from: $from\n    sortingAscending: $sortingAscending\n    sortingType: $sortingType\n    categories: $categories\n    orCategories: $orCategories\n    brands: $brands\n    orBrands: $orBrands\n    groups: $groups\n    orGroups: $orGroups\n    filters: $filters\n    tags: $tags\n    orTags: $orTags\n    withAllCategories: $withAllCategories\n    withAllSubCategories: $withAllSubCategories\n    withAllBrands: $withAllBrands\n    withOnlyGivenCategory: $withOnlyGivenCategory\n    inStock: $inStock\n  ) {\n    products {\n      ...ProductModel\n    }\n    categories {\n      categoryId\n      nameTr\n      slugTr\n      parentCategoryId\n    }\n    brands {\n      brandId\n      nameTr\n      slugTr\n    }\n    categoriesTree {\n      subCategories {\n        categoryId\n        parentCategoryId\n        nameTr\n        slugTr\n        subCategories {\n          categoryId\n          parentCategoryId\n          nameTr\n          slugTr\n        }\n      }\n    }\n    tags {\n      id\n      url\n      nameTr\n      nameEn\n      slugTr\n    }\n  }\n}\n\nfragment ProductModel on Product {\n    productId\n    suitableForCargo\n    name\n    nameTr\n    imageUrl\n    imageUrls\n    imagePath\n    description\n    descriptionHtml\n    fullPriceStr\n    fullPrice\n    taxRate\n    taxToPay\n    taxToPayStr\n    price\n    priceStr\n    tags\n    slug\n    maxAllowedInCart\n    noDiscount\n    tags2 {\n        id,\n        url,\n        nameTr\n        slugTr\n    }\n    listingTag {\n        id,\n        url,\n        nameTr\n        slugTr\n    }\n    discountRate\n    fullDiscountRate\n    productStock\n    qty\n    categories {\n        categoryId\n        parentCategoryId\n        nameTr\n        slugTr\n    }\n    brands {\n        brandId\n        nameTr\n        slugTr\n    }\n    promotions {\n        badge\n        promotionId\n    }\n}\n",
        "variables":{"token":"","addressId":None,"lat":41.00657,"lon":29.08852,"withAllBrands":True,"withAllCategories":True,"withAllSubCategories":False,"withOnlyGivenCategory":False,"size":1000,"from":0,"categories":[url],"brands":[],"groups":[],"tags":[]}})
       
        scraper = Scraper()
        
        try:
 
            response_get = scraper.POST(url="https://prod.fasapi.net/", body=post_body_data)

            #time.sleep(5)

            #soup = BeautifulSoup(response_get.text, "lxml")
        
        except Exception as e:

            print("IsteGelsinCrawler İnnerHtml Error: {}".format(e))

        return response_get if response_get else False
            

    
    def html_parser(self, html, crawler_config, page_category, url):

        p1 = crawler_config.p1
        p2 = crawler_config.p2
        p3 = crawler_config.p3
        p4 = crawler_config.p4
        p5 = crawler_config.p5
        p6 = crawler_config.p6
        p7 = crawler_config.p7
        p8 = crawler_config.p8
        p9 = crawler_config.p9
        p10 = crawler_config.p10
        p11 = crawler_config.p11
        products_and_price = []

        body = json.loads(html.content)
        products = body[eval(p1)][eval(p2)][eval(p3)]

        try:

            for product in products:

                articleName = product[eval(p4)]
                articleURL = "https://www.istegelsin.com/urun/" + product[eval(p5)]
                articleImage = product[eval(p6)] + "medium/" + product[eval(p7)] + ".webp"
                articlePrice = float(product[eval(p8)])
                sub_category = page_category
                articleMeas_get = articleName.strip().split(" ")
                
                if len(articleMeas_get)>1:

                    articleMeas = str(articleMeas_get[-2]) + " " + str(articleMeas_get[-1])

                sub_categories = product[eval(p9)]

                for s_category in sub_categories:

                    if s_category[eval(p10)] == url:

                        sub_category = s_category[eval(p11)]

                # assignment articles
                product_detail = {
                    'product_id': str(uuid.uuid4().hex),
                    'sub_category': sub_category,
                    'product_name': articleName,
                    'product_url': articleURL,
                    'measurement_value': articleMeas,
                    'currenct_unit': 'tl',
                    'price': articlePrice,
                    'image': articleImage
                }

                products_and_price.append(product_detail)
        
        except Exception as e:
            print("Articles error: {}".format(e))
        
        return products_and_price if products_and_price else False