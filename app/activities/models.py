from django.db import models
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.


class Activities(models.Model):

	name = models.CharField(max_length=120, null=False, blank=None, verbose_name='Activity Name')
	use_personal = models.BooleanField(default=0)
	status = models.BooleanField(default=1)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created Date', editable=False, null=True, blank=None)
	updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated Date', editable=False, null=True, blank=None)

	class Meta:
		verbose_name = 'Activities'
		verbose_name_plural = 'Activity'
	
	def __str__(self):
		return "%s" % self.name


class ActivityCategory(models.Model):

	activity = models.ForeignKey(Activities, null=None, related_name='activitiy_categories_relation_activitiy', on_delete=models.CASCADE, default=1)
	name = models.CharField(max_length=120, null=False, blank=None, verbose_name='Activity Category Name')
	image = models.TextField(null=True, blank=True)
	status = models.BooleanField(default=1)

	class Meta:
		verbose_name = 'ActivityCategories'
		verbose_name_plural = 'ActivityCategory'
	
	def __str__(self):
		return "%s" % self.name


class ActivitySubCategory(models.Model):
	activity = models.ForeignKey(Activities, null=None, related_name='ActivitySubCategory_activitiy_name', on_delete=models.CASCADE)
	activity_category = ChainedForeignKey(ActivityCategory, chained_field="activity", chained_model_field="activity", show_all=False, auto_choose=True, default=1)
	name = models.CharField(max_length=120, null=False, blank=None, verbose_name='Activity Sub Category Name')
	status = models.BooleanField(default=1)

	class Meta:
		verbose_name = 'ActivitySubCategory'
		verbose_name_plural = 'ActivitySubCategory'
	
	def __str__(self):
		return "%s" % self.name
