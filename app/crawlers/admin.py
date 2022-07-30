import imp
from django.contrib import admin
from crawlers.models import Crawlers, CrawlersConfig, CrawlerError
# Register your models here.

@admin.register(Crawlers)
class CrawlersAdmin(admin.ModelAdmin):

  list_display = ['company', 'demand', 'activity', 'activity_category', 'page_name']
  list_filter = ['company', 'demand',  'activity', 'activity_category', 'status']

    
  class Meta:
    model = Crawlers


@admin.register(CrawlersConfig)
class CrawlersAdmin(admin.ModelAdmin):

  list_display = ['company', 'demand', 'activity']
  list_filter = ['company']

    
  class Meta:
    model = CrawlersConfig


@admin.register(CrawlerError)
class CrawlersAdmin(admin.ModelAdmin):

  list_display = ['crawler_id', 'created_at']
  list_filter = ['created_at']

    
  class Meta:
    model = CrawlerError

