from itertools import product
from shutil import ExecError
from products.service import ProductsService
from companies.service import CompaniesService
from activities.service import ActivitiesService
from mongo.services import MongoService
from vendor.math import math_functions
from statistics import mean
import json


class DashboardService(object):

    def price_information_of_the_activities(self, activity, activity_category=None):

        try:

            results = [{
                "label": "Price information",
            }]

            if activity_category:

                results[0]["sub_label"] = "Price information for {}.".format(activity_category.lower())

            else:
                
                results[0]["sub_label"] = "Price information for {}.".format(activity.name.lower())

            return results

        except Exception as e:
            print("DashboardService price_information_of_the_activities Excepiton: {}".format(e))


    def number_of_products_for_activities(self, activity, activity_category=None):

        try:

            results = [{
                "label": "Number of Products",
            }]

            if activity_category:

                results[0]["sub_label"] = "Number of products in the {}.".format(activity_category.lower())

            else:

                results[0]["sub_label"] = "Number of products in the {}.".format(activity.name.lower())

            return results

        except Exception as e:
            print("DashboardService number_of_products_for_activities Excepiton: {}".format(e))


    def number_of_companies_for_activities(self, activity, activity_category=None):

        try:

            results = [{
                "label": "Number of Companies",
                "data": [{
                    "company_count":0
                }],
            }]

            if activity_category:

                results[0]["sub_label"] = "Number of company in the {}.".format(activity_category.lower())

                get_activity_category = ActivitiesService().get_activity_category(activity=activity, activity_category=activity_category)

                companies = ProductsService().get_companies(activity=activity, activity_category=get_activity_category)

            else:

                results[0]["sub_label"] = "Number of company in the {}.".format(activity.name.lower())

                companies = ProductsService().get_companies(activity=activity)


            company_count = len(companies) if companies else 0

            results[0]["data"][0]["company_count"] = company_count

            return results

        except Exception as e:
            print("DashboardService number_of_companies_for_activities Excepiton: {}".format(e))


    def category_based_statistics_of_companies_for_activities(self, activity, activity_category=None, main_company=None):

        try:

            results = [{
                "label": "Descriptive statistics for companies",
                "data": [],
                "main_company": [],
                "pie_data": [],
                "pie_labels": [],
                "main_company_activity_category_pie_data": [],
                "main_company_activity_category_pie_labels": [],
                

            }]

            if activity_category:
                
                results[0]["sub_label"] = "Sub category based statistics of companies for {}".format(activity_category.lower()),
                results[0]["main_company_activity_category_pie_title"] = "Sub Category distribution of your company"

                get_activity_category = ActivitiesService().get_activity_category(activity=activity, activity_category=activity_category)

                query = {"activity": activity, "activity_category": get_activity_category}

                get_all_companies_for_activity = ProductsService().get_companies(**query)

                get_all_activity_category_for_activity = ProductsService().get_unique_sub_categories_by_filter(**query)


            else:
                
                results[0]["sub_label"] = "Category based statistics of companies for {}".format(activity.name.lower()),
                results[0]["main_company_activity_category_pie_title"] = "Category distribution of your company"
                
                query = {"activity": activity}

                get_all_companies_for_activity = CompaniesService().get_companies_by_activity(**query)

                get_all_activity_category_for_activity = ActivitiesService().get_activity_categories(**query)

            if get_all_companies_for_activity:

                for company_name in get_all_companies_for_activity:

                    if type(company_name) is dict:
                        
                        company = CompaniesService().get_company_by_id(company=company_name["company"])
                       
                    else:

                        company = CompaniesService().get_company_by_name(company=company_name)

                    data = {
                            "company_name": company.page_name,
                            "company_logo": company.logo,
                            "comany_html_id": company.name,
                            "activity_category_detail": []
                        }
                    
                    for activity_category in get_all_activity_category_for_activity:
                        
                        if type(activity_category) is dict:
                            activity_category = activity_category["sub_category"]
                            info_activity_category = activity_category
                            mongo_query = MongoService().avg_price_query_generator(get_id="sub_category", activity=activity, sub_category=activity_category, company=company.name)
                           
                        else:
                            info_activity_category = activity_category.name
                            mongo_query = MongoService().avg_price_query_generator(get_id="activity_category", activity=activity, activity_category=activity_category, company=company.name)

                        activity_category_product_statistics_data = MongoService().get_avg_data(collection=activity, query=mongo_query)

                        if len(activity_category_product_statistics_data) > 0:

                            if type(activity_category_product_statistics_data[0]["_id"]) is list:

                                get_mongo_activity_category = activity_category_product_statistics_data[0]["_id"][0]
                                mongo_activity_category = get_mongo_activity_category.replace("_", " ").capitalize()
                            else:
                                mongo_activity_category = activity_category_product_statistics_data[0]["_id"].replace("_", " ").capitalize()
                           
                            activity_category_detail = {
                                "activity_category": info_activity_category.replace("_", " ").capitalize()  if activity_category_product_statistics_data[0]["_id"] == None else mongo_activity_category,
                                "product_count": activity_category_product_statistics_data[0]["count"],
                                "min_price": round(min(activity_category_product_statistics_data[0]["minPrice"]), 3) if type(activity_category_product_statistics_data[0]["minPrice"]) == list else activity_category_product_statistics_data[0]["minPrice"],
                                "max_price": round(max(activity_category_product_statistics_data[0]["maxPrice"]), 3) if type(activity_category_product_statistics_data[0]["maxPrice"]) == list else activity_category_product_statistics_data[0]["maxPrice"],
                                "avg_price": round(activity_category_product_statistics_data[0]["averagePrice"], 3) if activity_category_product_statistics_data[0]["averagePrice"] else None,
                            }

                        else:

                            activity_category_detail = {
                                "activity_category": info_activity_category.replace("_", " ").capitalize()  if type(activity_category) is dict else info_activity_category.replace("_", " ").capitalize(),
                                "product_count": 0,
                                "min_price": 0,
                                "max_price": 0,
                                "avg_price": 0,
                            }

                        data["activity_category_detail"].append(activity_category_detail)
                
                    results[0]["data"].append(data)
                    
                    if main_company == company.name:
                        results[0]["main_company"].append(data)
                
                main_company_activity_category_pie_data = []
                main_company_activity_category_pie_labels = []
                for i in results[0]["data"]:
                    for a in i["activity_category_detail"]:

                        if main_company == i["comany_html_id"]:

                            main_company_activity_category_pie_data.append(a["product_count"])
                            main_company_activity_category_pie_labels.append(a["activity_category"])

                results[0]["main_company_activity_category_pie_data"] = main_company_activity_category_pie_data
                results[0]["main_company_activity_category_pie_labels"] = main_company_activity_category_pie_labels

                return results

            else:
                print("s")

        except Exception as e:
            print("DashboardService category_based_statistics_of_companies_for_activities Excepiton: {}".format(e))


    def product_distribution_of_companies_in_activities(self, activity, activity_category=None):

        try:

            results = [{
                "label": "Product Distrubition of Companies",
                "pie_colors": ["bg-info", "bg-success", "bg-primary", "bg-danger", "bg-blue", "bg-pink", "bg-green", "bg-gray-dark", "bg-purple", "bg-orange", "bg-cyan", "bg-gray", "bg-yellow"],
                "pie_data": [],
                "pie_labels": [],
                "data": [],
            }]

            if activity_category:

                results[0]["sub_label"] = "Product distribution of companies in {}.".format(activity_category.lower())
                
                get_activity_category = ActivitiesService().get_activity_category(activity=activity, activity_category=activity_category)

                query = {"activity": activity.id, "activity_category": get_activity_category.id}

                all_product_count = ProductsService().count_of_products_by_filter(**query)
                
                previous_all_product_count = ProductsService().count_of_products_by_filter(**query, week=True)

                get_all_companies_for_activity = ProductsService().get_companies(**query)


            else:

                results[0]["sub_label"] = "Product distribution of companies in {}.".format(activity.name.lower())

                query = {"activity": activity.id}

                all_product_count = ProductsService().count_of_products_by_filter(**query)
                
                previous_all_product_count = ProductsService().count_of_products_by_filter(**query, week=True)

                get_all_companies_for_activity = CompaniesService().get_companies_by_activity(**query)

            if get_all_companies_for_activity:

                for company_name in get_all_companies_for_activity:

                    if type(company_name) is dict:
                        
                        company = CompaniesService().get_company_by_id(company=company_name["company"])
                    
                    else:

                        company = CompaniesService().get_company_by_name(company=company_name)

                    query["company"] = company

                    company_product_count = ProductsService().count_of_products_by_filter(**query)

                    data = {
                        "company_name": company.page_name,
                        "product_count": company_product_count
                    }

                    results[0]["data"].append(data)

                results[0]["data"] = sorted(results[0]["data"], key=lambda x: x['product_count'], reverse=True)

                for d in results[0]["data"]:
                    results[0]["pie_labels"].append(d["company_name"])
                    results[0]["pie_data"].append(d["product_count"])

                results[0]["all_product_count"] = all_product_count
                results[0]["previous_all_product_count"] = previous_all_product_count
                results[0]["product_ratio"] = math_functions.rate_of_change(last=previous_all_product_count, now=all_product_count)
            
            else:

                results[0]["message"] = "We couldn't find any companies with products in this category."

            return results            

        except Exception as e:
            print("DashboardService product_distribution_of_companies_in_activities Exception: {}".format(e))


    def all_comparative_statistics_data_for_activities(self, activity, activity_category=None):

        try:

            results = [{
                "price_information": [],
                "sub_category_information": [],
                "product_information": [],
                
            }]

            if activity_category:
            
                get_activity_category = ActivitiesService().get_activity_category(activity=activity, activity_category=activity_category)

                # Product Info
                product_query = {"activity": activity.id, "activity_category": get_activity_category.id}

                recent_all_product_count = ProductsService().count_of_products_by_filter(**product_query)
                
                previous_all_product_count = ProductsService().count_of_products_by_filter(**product_query, week=True)

                # Price Info
                recent_price_query = MongoService().avg_price_query_generator(get_id='activity_category', activity=activity, activity_category=get_activity_category)

                previous_price_query = MongoService().avg_price_query_generator(get_id="activity_category", activity=activity, activity_category=activity_category, week=True)

                # Sub Categıry

                sub_category_query = {"activity": activity.id, "activity_category": get_activity_category.id}
                
                recent_sub_category_count = ProductsService().get_unique_sub_categories_by_filter(**sub_category_query)

                previous_sub_category_count = ProductsService().get_unique_sub_categories_by_filter(**sub_category_query, week=True)


            else:

                # Product Info
                product_query = {"activity": activity.id}

                recent_all_product_count = ProductsService().count_of_products_by_filter(**product_query)
                
                previous_all_product_count = ProductsService().count_of_products_by_filter(**product_query, week=True)

                # Price Info
                recent_price_query = MongoService().avg_price_query_generator(get_id='activity', activity=activity)

                previous_price_query = MongoService().avg_price_query_generator(get_id="activity", activity=activity, week=True)

                # Sub Categıry

                sub_category_query = {"activity": activity.id}
                
                recent_sub_category_count = ProductsService().get_unique_sub_categories_by_filter(**sub_category_query)

                previous_sub_category_count = ProductsService().get_unique_sub_categories_by_filter(**sub_category_query, week=True)

            product_information = {
                "recent_all_product_count": recent_all_product_count,
                "previous_all_product_count": previous_all_product_count,
                "ratio": math_functions.rate_of_change(last=previous_all_product_count, now=recent_all_product_count)
            }

            results[0]["product_information"].append(product_information)


            sub_category_information = {
                "recent_sub_category_count": len(recent_sub_category_count) if recent_sub_category_count else 0,
                "previous_sub_category_count": len(previous_sub_category_count) if previous_sub_category_count else 0,
            }

            sub_category_information["ratio"] = math_functions.rate_of_change(last=sub_category_information["previous_sub_category_count"], now=sub_category_information["recent_sub_category_count"])

            results[0]["sub_category_information"].append(sub_category_information)

            # BEGIN: Recent Price Info
            data = MongoService().get_avg_data(collection=activity, query=recent_price_query)
            
            if len(data) > 0:
                
                price_info = {
                    "min_price": round(min(data[0]["minPrice"]), 3) if type(data[0]["minPrice"]) == list else data[0]["minPrice"],
                    "max_price": round(max(data[0]["maxPrice"]), 3) if type(data[0]["maxPrice"]) == list else data[0]["maxPrice"],
                    "avg_price": round(data[0]["averagePrice"], 3) if data[0]["averagePrice"] else None,
                    "product_count": data[0]["count"] if data[0]["count"] else None,
                }

            else:

                price_info = { "min_price": 0, "max_price": 0, "avg_price": 0, "product_count": 0}

            results[0]["price_information"].append(price_info)

            # END: Recent Price Info


            # BEGIN: Previous Price Info
            previous_data = MongoService().get_avg_data(collection=str(activity), query=previous_price_query)

            if len(previous_data) > 0:

                previous_price_info = {
                    "min_price": round(min(previous_data[0]["minPrice"]), 3) if type(previous_data[0]["minPrice"]) == list else previous_data[0]["minPrice"],
                    "max_price": round(max(previous_data[0]["maxPrice"]), 3) if type(previous_data[0]["maxPrice"]) == list else previous_data[0]["maxPrice"],
                    "avg_price": round(previous_data[0]["averagePrice"], 3) if previous_data[0]["averagePrice"] else None,
                    "product_count": previous_data[0]["count"] if previous_data[0]["count"] else None,
                }

            else:

                previous_price_info = { "min_price": 0, "max_price": 0, "avg_price": 0, "product_count": 0}

            price_ratio = {
                "min_price": math_functions.rate_of_change(last=previous_price_info["min_price"], now=price_info["min_price"]),
                "max_price": math_functions.rate_of_change(last=previous_price_info["max_price"], now=price_info["max_price"]),
                "avg_price": math_functions.rate_of_change(last=previous_price_info["avg_price"], now=price_info["avg_price"])
            }

            results[0]["price_information"].append(previous_price_info)
            results[0]["price_information"].append(price_ratio)
            # END: Previous Price Info

            return results

                

        except Exception as e:
            print("DashboardService all_comparative_statistics_data_for_activities Exception: {}".format(e))


    def comparative_statistics_on_activity_for_the_main_company(self, main_company, activity, activity_category=None):

        try:

            results = [{
                "price_information": [],
                "sub_category_information": [],
                "product_information": []
            }]

            company = CompaniesService().get_company_by_name(main_company)

            if activity_category:
            
                get_activity_category = ActivitiesService().get_activity_category(activity=activity, activity_category=activity_category)

                # Product Info
                product_query = {"activity": activity.id, "activity_category": get_activity_category.id, "company": company.id}

                recent_all_product_count = ProductsService().count_of_products_by_filter(**product_query)
                
                previous_all_product_count = ProductsService().count_of_products_by_filter(**product_query, week=True)

                # Price Info
                recent_price_query = MongoService().avg_price_query_generator(get_id='activity_category', activity=activity, activity_category=get_activity_category, company=company)

                previous_price_query = MongoService().avg_price_query_generator(get_id="activity_category", activity=activity, activity_category=activity_category, company=company,week=True)

                # Sub Categıry

                sub_category_query = {"activity": activity.id, "activity_category": get_activity_category.id, "company": company.id}
                
                recent_sub_category_count = ProductsService().get_unique_sub_categories_by_filter(**sub_category_query)

                previous_sub_category_count = ProductsService().get_unique_sub_categories_by_filter(**sub_category_query, week=True)


            else:

                # Product Info
                product_query = {"activity": activity.id, "company": company.id}

                recent_all_product_count = ProductsService().count_of_products_by_filter(**product_query)
                
                previous_all_product_count = ProductsService().count_of_products_by_filter(**product_query, week=True)

                # Price Info
                recent_price_query = MongoService().avg_price_query_generator(get_id='activity', activity=activity, company=company)

                previous_price_query = MongoService().avg_price_query_generator(get_id="activity", activity=activity, company=company, week=True)

                # Sub Categıry

                sub_category_query = {"activity": activity.id, "company": company.id}
                
                recent_sub_category_count = ProductsService().get_unique_sub_categories_by_filter(**sub_category_query)

                previous_sub_category_count = ProductsService().get_unique_sub_categories_by_filter(**sub_category_query, week=True)

            product_information = {
                "recent_all_product_count": recent_all_product_count,
                "previous_all_product_count": previous_all_product_count,
                "ratio": math_functions.rate_of_change(last=previous_all_product_count, now=recent_all_product_count)
            }

            results[0]["product_information"].append(product_information)


            sub_category_information = {
                "recent_sub_category_count": len(recent_sub_category_count) if recent_sub_category_count else 0,
                "previous_sub_category_count": len(previous_sub_category_count) if previous_sub_category_count else 0,
            }

            sub_category_information["ratio"] = math_functions.rate_of_change(last=sub_category_information["previous_sub_category_count"], now=sub_category_information["recent_sub_category_count"])

            results[0]["sub_category_information"].append(sub_category_information)

            # BEGIN: Recent Price Info
            data = MongoService().get_avg_data(collection=activity, query=recent_price_query)
            
            if len(data) > 0:
                
                price_info = {
                    "min_price": round(min(data[0]["minPrice"]), 3) if type(data[0]["minPrice"]) == list else data[0]["minPrice"],
                    "max_price": round(max(data[0]["maxPrice"]), 3) if type(data[0]["maxPrice"]) == list else data[0]["maxPrice"],
                    "avg_price": round(data[0]["averagePrice"], 3) if data[0]["averagePrice"] else None,
                    "product_count": data[0]["count"] if data[0]["count"] else None,
                }

            else:

                price_info = { "min_price": 0, "max_price": 0, "avg_price": 0, "product_count": 0}

            results[0]["price_information"].append(price_info)

            # END: Recent Price Info


            # BEGIN: Previous Price Info
            previous_data = MongoService().get_avg_data(collection=str(activity), query=previous_price_query)

            if len(previous_data) > 0:

                previous_price_info = {
                    "min_price": round(min(previous_data[0]["minPrice"]), 3) if type(previous_data[0]["minPrice"]) == list else previous_data[0]["minPrice"],
                    "max_price": round(max(previous_data[0]["maxPrice"]), 3) if type(previous_data[0]["maxPrice"]) == list else previous_data[0]["maxPrice"],
                    "avg_price": round(previous_data[0]["averagePrice"], 3) if previous_data[0]["averagePrice"] else None,
                    "product_count": previous_data[0]["count"] if previous_data[0]["count"] else None,
                }

            else:

                previous_price_info = { "min_price": 0, "max_price": 0, "avg_price": 0, "product_count": 0}

            
            price_ratio = {
                "min_price": math_functions.rate_of_change(last=previous_price_info["min_price"], now=price_info["min_price"]),
                "max_price": math_functions.rate_of_change(last=previous_price_info["max_price"], now=price_info["max_price"]),
                "avg_price": math_functions.rate_of_change(last=previous_price_info["avg_price"], now=price_info["avg_price"])
            }

            results[0]["price_information"].append(previous_price_info)
            results[0]["price_information"].append(price_ratio)

            # END: Previous Price Info

            return results

                

        except Exception as e:
            print("DashboardService all_comparative_statistics_data_for_activities Exception: {}".format(e))


    def average_prices_of_companies_by_activities(self, activity, activity_category=None, main_company=None):

        try:

            results = [{
                "label": "Average prices of companies",
                "data": [],
                "main_company": [],
                "main_company_pie_data": [],
                "pie_data": [],
                "pie_labels": [],
                

            }]

            if activity_category:

                results[0]["sub_label"] = "Average prices of companies in category {}".format(activity_category.lower()),

                get_activity_category = ActivitiesService().get_activity_category(activity=activity, activity_category=activity_category)

                query = {"activity": activity, "activity_category": get_activity_category}

                get_all_companies_for_activity = ProductsService().get_companies(**query)


            else:
                
                results[0]["sub_label"] = "Average prices of companies in category {}".format(activity.name.lower()),
                
                query = {"activity": activity}

                get_all_companies_for_activity = CompaniesService().get_companies_by_activity(**query)

            if get_all_companies_for_activity:

                for company_name in get_all_companies_for_activity:

                    if type(company_name) is dict:
                        
                        company = CompaniesService().get_company_by_id(company=company_name["company"])
                        mongo_query = MongoService().avg_price_query_generator(get_id="activity_category", activity=activity, activity_category=get_activity_category, company=company.name)
                       
                    else:

                        company = CompaniesService().get_company_by_name(company=company_name)
                        mongo_query = MongoService().avg_price_query_generator(get_id="activity", activity=activity, company=company.name)

                    get_activities_statistics_data = MongoService().get_avg_data(collection=activity, query=mongo_query)

                    if len(get_activities_statistics_data) > 0:

                        activity_category_detail = {
                            "activity_category": get_activity_category.name if activity_category else activity,
                            "product_count": get_activities_statistics_data[0]["count"],
                            "min_price": round(min(get_activities_statistics_data[0]["minPrice"]), 3) if type(get_activities_statistics_data[0]["minPrice"]) == list else get_activities_statistics_data[0]["minPrice"],
                            "max_price": round(max(get_activities_statistics_data[0]["maxPrice"]), 3) if type(get_activities_statistics_data[0]["maxPrice"]) == list else get_activities_statistics_data[0]["maxPrice"],
                            "avg_price": round(get_activities_statistics_data[0]["averagePrice"], 3) if get_activities_statistics_data[0]["averagePrice"] else 0,
                            }

                    else:

                        activity_category_detail = {
                            "activity_category": get_activity_category.name if activity_category else activity,
                            "product_count": 0,
                            "min_price": 0,
                            "max_price": 0,
                            "avg_price": 0,
                        }

                    data = {
                        "company": company.name,
                        "company_name": company.page_name,
                        "logo": company.logo,
                        "avg_price": activity_category_detail["avg_price"],
                        "max_price": activity_category_detail["max_price"],
                        "min_price": activity_category_detail["min_price"],
                        "product_count": activity_category_detail["product_count"]
                    }

                    if main_company == company.name:
                        results[0]["main_company"].append(data)
                        main_company_avg_price = data["avg_price"]

                    if main_company is None:
                        main_company_avg_price = 0

                    

                    
                    results[0]["data"].append(data)
                    results[0]["pie_data"].append(data["avg_price"])
                    results[0]["pie_labels"].append(data["company_name"])

                for p_data in results[0]["pie_data"]:

                    results[0]["main_company_pie_data"].append(main_company_avg_price)

                return results

            else:

                print("s")

        except Exception as e:
            print("DashboardService average_prices_of_companies_by_activities Excepiton: {}".format(e))









  
    def get_last_update_activity_date(self, activity):

        try:

            update_date = ProductsService().get_last_update_at(activity=activity)
            return update_date

        
        except Exception as e:
            print("DashboardService get_last_update_activity_date Exception: {}".format(e))
