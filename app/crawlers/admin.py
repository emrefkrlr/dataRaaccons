import imp
from django.contrib import admin
from crawlers.models import Crawlers
# Register your models here.

@admin.register(Crawlers)
class CrawlersAdmin(admin.ModelAdmin):

  list_display = ['company', 'demand', 'activity', 'activity_category', 'page_name']
  list_filter = ['company', 'demand',  'activity', 'activity_category', 'status']

    
  class Meta:
    model = Crawlers

