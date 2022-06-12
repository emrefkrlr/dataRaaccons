from django.contrib import admin
from products.models import Products, ProductMatches

# Register your models here.

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):

  list_display = ['company', 'activity', 'activity_category', 'product_name', 'sub_category']
  list_filter = ['company', 'activity', 'activity_category','sub_category']

    
  class Meta:
    model = Products


@admin.register(ProductMatches)
class ProductsMatchesAdmin(admin.ModelAdmin):

  list_display = ['first_company_id', 'first_product_name', 'second_company_id', 'second_product_name', 'matched_score']

    
  class Meta:
    model = ProductMatches
