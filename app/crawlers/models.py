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
	created_at = models.DateTimeField(auto_created=True, verbose_name='Created Date', editable=False, null=True, blank=None)
	updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Updated Date', editable=False, null=True, blank=None)

	class Meta:
		
		verbose_name = 'Crawlers'
		verbose_name_plural = 'Crawler'
	

	def __str__(self):
		return "%s" % self.activity_category


