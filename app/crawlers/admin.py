import imp
from django.contrib import admin
from crawlers.models import Crawlers
# Register your models here.

@admin.register(Crawlers)
class CrawlersAdmin(admin.ModelAdmin):

  list_display = ['company', 'activity', 'demand', 'page_name', 'category']
  list_filter = ['company', 'activity', 'demand', 'page_name']

    
  class Meta:
    model = Crawlers

