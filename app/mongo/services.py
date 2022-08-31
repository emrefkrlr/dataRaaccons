from unittest import result
from pymongo import MongoClient, errors
from django.conf import settings
from datetime import datetime, timedelta
import os


class MongoService(object):


	def get_db_handle(self, db_name=None, host=None, port=None, username=None, password=None):

		try:
			#client = MongoClient(settings.MONGO_URI)
			client = MongoClient(host=settings.MONGO_HOST, port=int(settings.MONGO_PORT), username=settings.MONGO_USER, password=settings.MONGO_PASSWORD)
			db_handle = client[str(settings.MONGO_DB)]
			print("\n\n\nDB HANDLE: {}\n\n\n".format(db_handle))
			return db_handle, client
		
		except Exception as e:
			print("\nExeption get_db_handle: \n{}".format(e))


	def insert_one(self, collection, document):
		
		try:
		
			my_client = self.get_db_handle()
			dbname = my_client[0]
			collection_name = dbname[str(collection)]
			insert = collection_name.insert_one(document)
			
			return insert.inserted_id

		except Exception as e:
			print("\nExeption: \n{}".format(e))


	def insert_many(self, db_name, host, port, username, password, collection, document):
		
		try:
			my_client = MongoService().get_db_handle(db_name, host, port, username, password)
			dbname = my_client[0]
			collection_name = dbname[collection]
			insert = collection_name.insert_many(document)
			
			return insert.inserted_ids

		except Exception as e:
			print("\nExeption: \n{}".format(e))

	
	def find_one(self, db_name, host, port, username, password, collection, query=None):
		
		try:
			my_client = MongoService().get_db_handle(db_name, host, port, username, password)
			dbname = my_client[0]
			collection_name = dbname[collection]
			get_data = collection_name.find_one(query, sort=[( '_id', -1 )])
			return get_data

		except Exception as e:
			print("\nExeption: \n{}".format(e))


	def find(self, db_name, host, port, username, password, collection, query=None, distinct=None):
		
		try:
			my_client = MongoService().get_db_handle(db_name, host, port, username, password)
			dbname = my_client[0]
			collection_name = dbname[collection]
			if distinct:
				get_data = collection_name.find(query, sort=[( '_id', -1 )]).distinct(distinct)
			else:
				get_data = collection_name.find(query, sort=[( '_id', -1 )])
				
			return get_data

		except Exception as e:
			print("\nExeption: \n{}".format(e))

	def distinct(self,db_name, host, port, username, password, collection, query=None, distinct=None, key=None):

		try:
			my_client = MongoService().get_db_handle(db_name, host, port, username, password)
			dbname = my_client[0]
			collection_name = dbname[collection]
			get_data = collection_name.runCommand({ distinct: distinct, key: key, query: query })

			return get_data
			
			

		except Exception as e:
			print("\nExeption: \n{}".format(e))
	
	def aggregate(self, db_name, host, port, username, password, collection, aggregate):
		
		try:
			my_client = MongoService().get_db_handle(db_name, host, port, username, password)
			dbname = my_client[0]
			collection_name = dbname[collection]
			get_data = collection_name.aggregate(aggregate)
			return get_data

		except Exception as e:
			print("\nExeption: \n{}".format(e))


	def update_one(self, db_name, host, port, username, password, collection, target, value):
		
		try:
			if (target.values() is not None) or (value.values() is not None):
				
				my_client = MongoService().get_db_handle(db_name, host, port, username, password)
				dbname = my_client[0]
				collection_name = dbname[collection]
				update_data = collection_name.update_one(target, value)
				return update_data.matched_count > 0 

			else:
				raise Exception('dictionary is null')

		except errors.PyMongoError as e:
			print("\nExeption: \n{}".format(e))
			return False

		except Exception as e:
			print("\nExeption: \n{}".format(e))

	
	def delete_one(self, db_name, host, port, username, password, collection, target):
		
		try:
			if target.values() is not None:
				
				my_client = MongoService().get_db_handle(db_name, host, port, username, password)
				dbname = my_client[0]
				collection_name = dbname[collection]
				delete = collection_name.delete_one(target)
				return delete.deleted_count > 0

			else:
				raise Exception('dictionary is null')

		except errors.PyMongoError as e:
			print("\nExeption: \n{}".format(e))
			return False

		except Exception as e:
			print("\nExeption: \n{}".format(e))


	# Check
	def price_average_for_sub_categories(self, db_name, host, port, username, password, collection, activity_category):
		
		try:
			my_client = MongoService().get_db_handle(db_name, host, port, username, password)
			dbname = my_client[0]
			collection_name = dbname[collection]
			last_five_days = datetime.now() - timedelta(days = int(5))
			query = [
            	{
                	"$unwind": "$products_and_price",
            	},
				{
					"$match": {"info.activity_category": str(activity_category), "info.crawled_time" : {"$gt": str(last_five_days)}},
				},
				{
					"$group": 
					{
						"_id": "$products_and_price.sub_category",
						"averagePrice": 
						{
							"$avg": "$products_and_price.price"
						},
						"minPrice":
						{
							"$min": "$products_and_price.price"
						},
						"maxPrice":
						{
							"$max": "$products_and_price.price"
						},
						"count": { "$sum": 1 }
					},
				},
				{
   					"$sort" : { "averagePrice": -1 }
  				}
        	]
			get_data = collection_name.aggregate(query)
			return get_data

		except Exception as e:
			print("\nExeption: \n{}".format(e))

	# USE
	def price_average_for_activity_categories(self, db_name, host, port, username, password, collection, activity):

		try:
			my_client = MongoService().get_db_handle(db_name, host, port, username, password)
			dbname = my_client[0]
			collection_name = dbname[collection]
			last_five_days = datetime.now() - timedelta(days = int(25))
			query = [
            	{
                	"$unwind": "$products_and_price",
            	},
				{
					"$match": {"info.activity": str(activity), "info.crawled_time" : {"$gt": str(last_five_days)}},
				},
				{
					"$group": 
					{
						"_id": "$info.activity_category",
						"averagePrice": 
						{
							"$avg": "$products_and_price.price"
						},
						"minPrice":
						{
							"$min": "$products_and_price.price"
						},
						"maxPrice":
						{
							"$max": "$products_and_price.price"
						},
						"count": { "$sum": 1 }
					},
				},
				{
   					"$sort" : { "averagePrice": -1 }
  				}
        	]
			get_data = collection_name.aggregate(query)
			return list(get_data)

		except Exception as e:
			print("\nExeption: \n{}".format(e))

	# USE
	def price_average_for_activity(self, db_name, host, port, username, password, collection, activity):

		try:
			my_client = MongoService().get_db_handle(db_name, host, port, username, password)
			dbname = my_client[0]
			collection_name = dbname[collection]
			last_five_days = datetime.now() - timedelta(days = int(25))
			query = [
            	{
                	"$unwind": "$products_and_price",
            	},
				{
					"$match": {"info.activity": str(activity), "info.crawled_time" : {"$gt": str(last_five_days)}},
				},
				{
					"$group": 
					{
						"_id": "$info.activity",
						"averagePrice": 
						{
							"$avg": "$products_and_price.price"
						},
						"minPrice":
						{
							"$min": "$products_and_price.price"
						},
						"maxPrice":
						{
							"$max": "$products_and_price.price"
						},
						"count": { "$sum": 1 }
					},
				},
				{
   					"$sort" : { "averagePrice": -1 }
  				}
        	]
			get_data = collection_name.aggregate(query)
			return list(get_data)

		except Exception as e:
			print("\nExeption: \n{}".format(e))

	# Check
	def price_average_of_activity_based_companies(self, db_name, host, port, username, password, collection, activity, company):

		try:
			my_client = MongoService().get_db_handle(db_name, host, port, username, password)
			dbname = my_client[0]
			collection_name = dbname[collection]
			last_five_days = datetime.now() - timedelta(days = int(25))

			query = [
            	{
                	"$unwind": "$products_and_price",
            	},
				{
					"$match": {"info.company_name": str(company), "info.activity": str(activity), "info.crawled_time" : {"$gt": str(last_five_days)}},
				},
				{
					"$group": 
					{
						"_id": "$info.company_name",
						"averagePrice": 
						{
							"$avg": "$products_and_price.price"
						},
						"minPrice":
						{
							"$min": "$products_and_price.price"
						},
						"maxPrice":
						{
							"$max": "$products_and_price.price"
						},
						"count": { "$sum": 1 }
					},
				},
				{
   					"$sort" : { "averagePrice": -1 }
  				}
        	]
			get_data = collection_name.aggregate(query)
			
			return list(get_data)
			
		except Exception as e:
			print("\nExeption: \n{}".format(e))

	# Check
	def price_average_of_activity_category_based_companies(self, db_name, host, port, username, password, collection, activity_category):

		try:
			my_client = MongoService().get_db_handle(db_name, host, port, username, password)
			dbname = my_client[0]
			collection_name = dbname[collection]
			last_five_days = datetime.now() - timedelta(days = int(25))
			query = [
            	{
                	"$unwind": "$products_and_price",
            	},
				{
					"$match": {"info.activity_category": str(activity_category), "info.crawled_time" : {"$gt": str(last_five_days)}},
				},
				{
					"$group": 
					{
						"_id": "$info.company_name",
						"averagePrice": 
						{
							"$avg": "$products_and_price.price"
						},
						"minPrice":
						{
							"$min": "$products_and_price.price"
						},
						"maxPrice":
						{
							"$max": "$products_and_price.price"
						},
						"count": { "$sum": 1 }
					},
				},
				{
   					"$sort" : { "averagePrice": -1 }
  				}
        	]
			get_data = collection_name.aggregate(query)
			return get_data

		except Exception as e:
			print("\nExeption: \n{}".format(e))

	# Check
	def price_average_of_sub_category_based_companies(self, db_name, host, port, username, password, collection, activity_category, sub_category):

		try:
			my_client = MongoService().get_db_handle(db_name, host, port, username, password)
			dbname = my_client[0]
			collection_name = dbname[collection]
			last_five_days = datetime.now() - timedelta(days = int(25))
			query = [
            	{
                	"$unwind": "$products_and_price",
            	},
				{
					"$match": {"info.activity_category": str(activity_category) ,"products_and_price.sub_category": str(sub_category), "info.crawled_time" : {"$gt": str(last_five_days)}},
				},
				{
					"$group": 
					{
						"_id": "$info.company_name",
						"averagePrice": 
						{
							"$avg": "$products_and_price.price"
						},
						"minPrice":
						{
							"$min": "$products_and_price.price"
						},
						"maxPrice":
						{
							"$max": "$products_and_price.price"
						},
						"count": { "$sum": 1 }
					},
				},
				{
   					"$sort" : { "averagePrice": -1 }
  				}
        	]
			get_data = collection_name.aggregate(query)
			return get_data

		except Exception as e:
			print("\nExeption: \n{}".format(e))

	# Use
	def price_average_for_activity_categories_based_company(self, db_name, host, port, username, password, collection, activity, activity_category, company):

		try:
			my_client = MongoService().get_db_handle(db_name, host, port, username, password)
			dbname = my_client[0]
			collection_name = dbname[collection]
			last_five_days = datetime.now() - timedelta(days = int(25))
			query = [
            	{
                	"$unwind": "$products_and_price",
            	},
				{
					"$match": {"info.company_name": str(company), "info.activity": str(activity), "info.activity_category": str(activity_category), "info.crawled_time" : {"$gt": str(last_five_days)}},
				},
				{
					"$group": 
					{
						"_id": "$info.activity_category",
						"averagePrice": 
						{
							"$avg": "$products_and_price.price"
						},
						"minPrice":
						{
							"$min": "$products_and_price.price"
						},
						"maxPrice":
						{
							"$max": "$products_and_price.price"
						},
						"count": { "$sum": 1 }
					},
				},
				{
   					"$sort" : { "averagePrice": -1 }
  				}
        	]
			get_data = collection_name.aggregate(query)

			
			return list(get_data)

		except Exception as e:
			print("\nExeption: \n{}".format(e))

	# Use
	def get_activity_based_average_prices_for_the_company(self, db_name, host, port, username, password, collection, activity, company):

		try:
			
			my_client = MongoService().get_db_handle(db_name, host, port, username, password)
			dbname = my_client[0]
			collection_name = dbname[collection]
			last_five_days = datetime.now() - timedelta(days = int(25))

			query = [
            	{
                	"$unwind": "$products_and_price",
            	},
				{
					"$match": {"info.company_name": str(company), "info.activity": str(activity), "info.crawled_time" : {"$gt": str(last_five_days)}},
				},
				{
					"$group": 
					{
						"_id": "$info.activity",
						"averagePrice": 
						{
							"$avg": "$products_and_price.price"
						},
						"minPrice":
						{
							"$min": "$products_and_price.price"
						},
						"maxPrice":
						{
							"$max": "$products_and_price.price"
						},
						"count": { "$sum": 1 }
					},
				},
				{
   					"$sort" : { "averagePrice": -1 }
  				}
        	]

			get_data = collection_name.aggregate(query)
			
			return list(get_data)

		except Exception as e:
			print("Mongo Service get_activity_based_average_prices_for_the_company Exception: \n{}".format(e))




	# Previous 

	def get_previous_price_avarage_activity(self, db_name, host, port, username, password, collection, activity, year=False, month=False, week=False):

		try:
			
			# default previous week

			if [year,month, week].count(True) > 1:

				return False

			else:

				current_date = datetime.now()

				if year:

					previous_date = current_date - timedelta(days= 365)

				elif month:

					previous_date = current_date - timedelta(days= 30)

				elif week:

					previous_date = current_date - timedelta(days= 7)
				
				else:

					previous_date = current_date - timedelta(days= 365)

			

				my_client = MongoService().get_db_handle(db_name, host, port, username, password)
				dbname = my_client[0]
				collection_name = dbname[collection]

				query = [
					{
						"$unwind": "$products_and_price",
					},
					{
						"$match": {"info.activity": str(activity), "info.crawled_time" : {"$gt": str(current_date), "$lt": str(previous_date)}},
					},
					{
						"$group": 
						{
							"_id": "$info.activity",
							"averagePrice": 
							{
								"$avg": "$products_and_price.price"
							},
							"minPrice":
							{
								"$min": "$products_and_price.price"
							},
							"maxPrice":
							{
								"$max": "$products_and_price.price"
							},
							"count": { "$sum": 1 }
						},
					},
					{
						"$sort" : { "averagePrice": -1 }
					}
				]
				
				get_data = collection_name.aggregate(query)
				
				return list(get_data)

		except Exception as e:
			print("Mongo Service get_previous_price_avarage_activity Exception : \n{}".format(e))


	def avg_price_query_generator(self, get_id, activity=None, activity_category=None, sub_category=None, company=None, year=False, month=False, week=False):

		try:

			current_date = datetime.now()

			query_match = {}
			query = [{ "$unwind": "$products_and_price", "$unwind": "$products_and_price"}, {"$match": query_match}]
			
			if activity:
				query_match["info.activity"] = str(activity)
			
			if activity_category:
				query_match["info.activity_category"] = str(activity_category)

			if sub_category:
				query_match["products_and_price.sub_category"] = str(sub_category)

				query_get_id = {
					"$group": 
					{
						"_id": "$products_and_price.{}".format(get_id), 
						"averagePrice": 
						{
							"$avg": "$products_and_price.price"
						},
						"minPrice":
						{
							"$min": "$products_and_price.price"
						},
						"maxPrice":
						{
							"$max": "$products_and_price.price"
						},
						"count": 
						{
							"$sum": 1
						}
					},
				}
				
			else:

				query_get_id = {
					"$group": 
					{
						"_id": "$info.{}".format(get_id), 
						"averagePrice": 
						{
							"$avg": "$products_and_price.price"
						},
						"minPrice":
						{
							"$min": "$products_and_price.price"
						},
						"maxPrice":
						{
							"$max": "$products_and_price.price"
						},
						"count": 
						{
							"$sum": 1
						}
					},
				}

			if company:
				query_match["info.company_name"] = str(company)

			if [year, month, week].count(True) == 1:
				
				if year:

					previous_date = current_date - timedelta(days= 365)

				elif month:
					
					previous_date = current_date - timedelta(days= 30)
				
				else:
					
					previous_date = current_date - timedelta(days= 7)

				query_match["info.crawled_time"] = {"$gt": str(current_date), "$lt": str(previous_date)}
				
			else:

				query_match["info.crawled_time"] = {"$gt": str(current_date  - timedelta(days= 365))}
				
			
			query.append(query_get_id)

			query_sort = {
				"$sort" : 
				{
					 "count": -1 
				}
			}
			
			query.append(query_sort)

			return query
		
		except Exception as e:
			print("Mongo Service avg_price_query_generator Exception : \n{}".format(e))

		
	def get_avg_data(self, collection, query):

		try:

			my_client = self.get_db_handle()
			dbname = my_client[0]
			collection_name = dbname[str(collection)]

			results = collection_name.aggregate(query)

			return list(results)
		
		except Exception as e:
			print("Mongo Service get_avg_data Exception: \n{}".format(e))


		