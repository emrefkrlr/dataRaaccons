from pyexpat import model
from django.db import models
from activities.models import Activities

# Create your models here.

class Companies(models.Model):

	name = models.CharField(max_length=120, null=False, blank=None, verbose_name='Company Name')
	page_name = models.CharField(max_length=120, null=True, blank=True, verbose_name='Company Page Name')
	url = models.CharField(max_length=255, null=True, blank=True, verbose_name='Company Main Url')
	logo = models.CharField(max_length=255, null=True, blank=True, verbose_name='Company Logo')
	status = models.BooleanField(default=1)
	created_at = models.DateTimeField(auto_created=True, verbose_name='Created Date', editable=False, null=True, blank=None)
	updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Updated Date', editable=False, null=True, blank=None)


	class Meta:
		verbose_name = 'Companies'
		verbose_name_plural = 'Company'
	

	def __str__(self):
		return "%s" % self.name


class CompanyActivities(models.Model):
	
	company = models.ForeignKey(Companies, null=None, related_name='companyies_name', on_delete=models.CASCADE)
	activity = models.ForeignKey(Activities, null=None, related_name='activities_name', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_created=True, verbose_name='Created Date', editable=False, null=True, blank=None)
	updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Updated Date', editable=False, null=True, blank=None)


	class Meta:
		verbose_name = 'Company Activities'
		verbose_name_plural = 'Company Activiy'
	

	def __str__(self):
		return "%s" % self.company