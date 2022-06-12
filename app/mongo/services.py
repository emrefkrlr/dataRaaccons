from pymongo import MongoClient, errors
import logging

logger = logging.getLogger(__name__)


class MongoService(object):


	def get_db_handle(self, db_name, host, port, username, password):

		try:
			client = MongoClient(host=host, port=int(port), username=username, password=password)
			db_handle = client[str(db_name)]
		
			return db_handle, client
		
		except Exception as e:
			print("\nExeption: \n{}".format(e))


	def insert_one(self, db_name, host, port, username, password, collection, document):
		
		try:
			my_client = MongoService().get_db_handle(db_name, host, port, username, password)
			dbname = my_client[0]
			collection_name = dbname[collection]
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
			get_data = collection_name.aggregate([aggregate])
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


	def get_sub_category_price(self, db_name, host, port, username, password, collection, query):

		try:
			my_client = MongoService().get_db_handle(db_name, host, port, username, password)
			dbname = my_client[0]
			collection_name = dbname[collection]

			get_data = collection_name.find(query, sort=[( '_id', -1 )]).limit(2)

			return get_data


		except Exception as e:
			print("\nExeption: \n{}".format(e))