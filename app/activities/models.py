from django.db import models

# Create your models here.


class Activities(models.Model):

	name = models.CharField(max_length=120, null=False, blank=None, verbose_name='Activity Name')
	status = models.BooleanField(default=1)
	created_at = models.DateTimeField(auto_created=True, verbose_name='Created Date', editable=False, null=True, blank=None)
	updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Updated Date', editable=False, null=True, blank=None)

	class Meta:
		verbose_name = 'Activities'
		verbose_name_plural = 'Activity'
	
	def __str__(self):
		return "%s" % self.name


class ActivityCategory(models.Model):

	activity = models.ForeignKey(Activities, null=None, related_name='activitiy_categories_relation_activitiy', on_delete=models.CASCADE, default=1)
	name = models.CharField(max_length=120, null=False, blank=None, verbose_name='Activity Category Name')
	status = models.BooleanField(default=1)

	class Meta:
		verbose_name = 'ActivityCategories'
		verbose_name_plural = 'ActivityCategory'
	
	def __str__(self):
		return "%s" % self.name
