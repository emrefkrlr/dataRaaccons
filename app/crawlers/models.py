from django.db import models
from companies.models import Companies
from activities.models import Activities
from demands.models import Demands

# Create your models here.


class Crawlers(models.Model):

	company = models.ForeignKey(Companies, null=None, related_name='company_name', on_delete=models.CASCADE)
	activity = models.ForeignKey(Activities, null=None, related_name='activitiy_name', on_delete=models.CASCADE)
	demand = models.ForeignKey(Demands, null=None, related_name='demands_name', on_delete=models.CASCADE)
	page_name = models.CharField(max_length=120, null=False, blank=None, verbose_name='Page Name')
	page_url = models.CharField(max_length=120, null=False, blank=None, verbose_name='Page Url')
	categor = models.CharField(max_length=120, null=True, blank=True, verbose_name='Category')
	css_selector = models.CharField(max_length=120, null=True, blank=True, verbose_name='Css Selector')
	page_numbers = models.IntegerField(default= 0, null=True, blank=True, verbose_name='Page Numbers')
	schedule = models.CharField(max_length=120, null=True, blank=True, verbose_name='Schedule Config')
	status = models.BooleanField(default=1)
	created_at = models.DateTimeField(auto_created=True, verbose_name='Created Date', editable=False, null=True, blank=None)
	updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Updated Date', editable=False, null=True, blank=None)

	class Meta:
		
		verbose_name = 'Crawlers'
		verbose_name_plural = 'Crawler'
	

	def __str__(self):
		return "%s" % self.page_url


