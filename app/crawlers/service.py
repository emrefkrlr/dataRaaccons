from crawlers.models import Crawlers


class CrawlerServices(object):

	def fetch_urls_to_crawl(self, filter):

		try:

			if bool(filter):
				results = Crawlers.objects.filter(**filter)
				return results
			else:
				raise Exception('dictionary is null')
		
		except Exception as e:
			print("\nExeption: \n{}".format(e))

	def get_unique_page_category(self, filter):

		try:

			if bool(filter):
				results = Crawlers.objects.filter(**filter).distinct('page_category')
				return results
			else:
				raise Exception('dictionary is null')
		
		except Exception as e:
			print("\nExeption: \n{}".format(e))

