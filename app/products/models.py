from email.mime import image
from itertools import product
from pyexpat import model
from django.db import models
from companies.models import Companies
from activities.models import Activities, ActivityCategory
# Create your models here.


class Products(models.Model):
    
    company = models.ForeignKey(Companies, null=None, related_name='prodcut_company_name', on_delete=models.CASCADE)
    activity = models.ForeignKey(Activities, null=None, related_name='product_activitiy_name', on_delete=models.CASCADE)
    activity_category = models.ForeignKey(ActivityCategory, null=None, related_name='product_main_category_name', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250, null=False, blank=None, verbose_name='Product Name')
    price = models.FloatField(default=0, null=True, blank=True, verbose_name="Product Price")
    page_category = models.CharField(max_length=250, null=False, blank=None, verbose_name='Page Category Name')
    sub_category = models.CharField(max_length=250, null=False, blank=None, verbose_name='Sub Category')
    image = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_created=True, verbose_name='Created Date', editable=False, null=True, blank=None)
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Updated Date', editable=False, null=True, blank=None)

    class Meta:
	
        verbose_name = 'Products'
        verbose_name_plural = 'Product'
	

    def __str__(self):
        return "%s" % self.product_name


class ProductMatches(models.Model):

    # FIRST PRODUCT INFO
    first_product_activity_category_id = models.IntegerField(null=None, blank=False, verbose_name='first_product_activity_category_id')
    first_company_id = models.IntegerField(null=None, blank=False, verbose_name='first_company_id')
    first_product_id = models.IntegerField(null=None, blank=False, verbose_name='first_product_id')
    first_product_name = models.CharField(max_length=250, null=False, blank=None, verbose_name='first_product_name')
    
    # SECOND PRODUCT INFO
    second_product_activity_category_id = models.IntegerField(null=None, blank=False, verbose_name='second_product_activity_category_id')
    second_company_id = models.IntegerField(null=None, blank=False, verbose_name='second_company_id')
    second_product_id = models.IntegerField(null=None, blank=False, verbose_name='first_product_id')
    second_product_name = models.CharField(max_length=250, null=False, blank=None, verbose_name='second_product_name')
    
    # MATCHED INFO
    matches_activity = models.ForeignKey(Activities, null=None, related_name='ProductMatches_matches_activity', on_delete=models.CASCADE)
    matched_score = models.FloatField(null=None, blank=False, verbose_name='Matched Score')    
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_created=True, verbose_name='Created Date', editable=False, null=True, blank=None)
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Updated Date', editable=False, null=True, blank=None)

    class Meta:
	
        verbose_name = 'ProductMatches'
        verbose_name_plural = 'ProductMatched'
	

    def __str__(self):
        return "%s" % self.first_product_name



    



