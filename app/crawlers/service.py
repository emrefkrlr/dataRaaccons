from crawlers.models import Crawlers, CrawlersConfig, CrawlerError, WebDriverConfig


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


	def get_crawler_config(self, company, activity):

		try:

			configs = CrawlersConfig.objects.get(company__name=company, activity__name=activity)
			return configs if configs else False

		except Exception as e:
			print("Crawler Service get_crawler_config EXCEPTION: {}".format(e))


	def insert_crawler_error(self, **kwargs):

		try:

			insert = CrawlerError.objects.get_or_create(kwargs)

			return insert if insert else False

		except Exception as e:
			print("Crawler Service set_crawler_error EXCEPTION: {}".format(e))

	def get_web_driver_address(self):

		try:

			web_driver = WebDriverConfig.objects.first()

			

			return str(web_driver)

		except Exception as e:
			print("Crawler Service get_web_driver_address EXCEPTION: {}".format(e))





