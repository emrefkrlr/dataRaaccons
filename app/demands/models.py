from django.db import models

# Create your models here.


class Demands(models.Model):

  
	name = models.CharField(max_length=120, null=False, blank=None, verbose_name='Demand Name')
	status = models.BooleanField(default=1)
	created_at = models.DateTimeField(auto_created=True, verbose_name='Created Date', editable=False, null=True, blank=None)
	updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Updated Date', editable=False, null=True, blank=None)

	class Meta:
		verbose_name = 'Demands'
		verbose_name_plural = 'Demand'
	
	def __str__(self):
		return "%s" % self.name