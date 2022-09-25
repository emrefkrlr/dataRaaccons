from pyexpat import model
from django.db import models
from companies.models import Companies
from activities.models import Activities, ActivityCategory
from demands.models import Demands
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.


class Crawlers(models.Model):
	
	# Crawler INFO
	company = models.ForeignKey(Companies, null=None, related_name='company_name', on_delete=models.CASCADE)
	demand = models.ForeignKey(Demands, null=None, related_name='demands_name', on_delete=models.CASCADE)
	activity = models.ForeignKey(Activities, null=None, related_name='activitiy_name', on_delete=models.CASCADE)
	# activity_category = models.ForeignKey(ActivityCategory, null=None, related_name='activity_category_name', on_delete=models.CASCADE)
	activity_category = ChainedForeignKey(ActivityCategory, chained_field="activity", chained_model_field="activity", show_all=False, auto_choose=True)
	
	# PAGE INFO
	page_url = models.CharField(max_length=255, null=False, blank=None, verbose_name='Page Url')
	page_numbers = models.IntegerField(default= 0, null=True, blank=True, verbose_name='Page Numbers')
	page_name = models.CharField(max_length=120, null=False, blank=None, verbose_name='Page Name')
	page_category = models.CharField(max_length=120, null=True, blank=True, verbose_name='Page Category')
	css_selector = models.CharField(max_length=120, null=True, blank=True, verbose_name='Css Selector')

	# SCHEDULE INFO
	schedule = models.CharField(max_length=120, null=True, blank=True, verbose_name='Schedule Config')
	status = models.BooleanField(default=1)
	created_at = models.DateTimeField(auto_now_add=True,  verbose_name='Created Date', editable=False,  null=True)
	updated_at = models.DateTimeField(auto_now=True,  verbose_name='Update Date', editable=False, null=True)

	class Meta:
		
		verbose_name = 'Crawlers'
		verbose_name_plural = 'Crawler'
	

	def __str__(self):
		return "%s" % self.activity_category


class CrawlersConfig(models.Model):
	
	company = models.ForeignKey(Companies, null=None, related_name='crawler_config_company_name', on_delete=models.CASCADE)
	demand = models.ForeignKey(Demands, null=None, related_name='crawler_config_demands_name', on_delete=models.CASCADE)
	activity = models.ForeignKey(Activities, null=None, related_name='crawler_config_activitiy_name', on_delete=models.CASCADE)
	css_selector = models.CharField(max_length=120, null=True, blank=True, verbose_name='Css Selector')
	p1 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p1')
	p2 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p2')
	p3 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p3')
	p4 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p4')
	p5 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p5')
	p6 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p6')
	p7 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p7')
	p8 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p8')
	p9 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p9')
	p10 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p10')
	p11 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p11')
	p12 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p12')
	p13 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p13')
	p14 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p14')
	p15 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p15')
	p16 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p16')
	p17 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p17')
	p18 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p18')
	p19 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p19')
	p20 = models.CharField(max_length=120, null=True, blank=True, verbose_name='p20')
	created_at = models.DateTimeField(auto_now_add=True,  verbose_name='Created Date', editable=False)
	updated_at = models.DateTimeField(auto_now=True,  verbose_name='Update Date', editable=False)

	class Meta:
		
		verbose_name = 'Crawler Config'
		verbose_name_plural = 'Crawler Config'
	

	def __str__(self):
		return "%s" % self.activity


class CrawlerError(models.Model):

	crawler_id = models.IntegerField(default= 0, null=True, blank=True, verbose_name='Crawler ID')
	error_message = models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True,  verbose_name='Created Date', editable=False)
	

	class Meta:
		
		verbose_name = 'Crawler Err'
		verbose_name_plural = 'Crawler Err'
	

	def __str__(self):
		return "%s" % self.crawler_id


class WebDriverConfig(models.Model):

	ip_address = models.CharField(max_length=120, null=True, blank=True, verbose_name='IP address')

	class Meta:
		
		verbose_name = 'WebDriver'
		verbose_name_plural = 'WebDriver'
	

	def __str__(self):
		return "%s" % self.ip_address


