from django.contrib import admin
from activities.models import Activities, ActivityCategory, ActivitySubCategory, MappingSubCategory

# Register your models here.


@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):

  list_display = ['name', 'status']
  list_filter = ['name', 'status']

    
  class Meta:
    model = Activities


@admin.register(ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):

  list_display = ['name', 'activity', 'status']
  list_filter = ['name','status']

    
  class Meta:
    model = ActivityCategory


@admin.register(ActivitySubCategory)
class ActivitySubCategoryAdmin(admin.ModelAdmin):

  list_display = ['name', 'activity_category']
  list_filter = ['name', 'activity_category', 'status']

    
  class Meta:
    model = ActivitySubCategory


@admin.register(MappingSubCategory)
class MappingSubCategoryAdmin(admin.ModelAdmin):

  list_display = ['mapping_activity_category', 'mapping_activity_sub_category', 'mongo_sub_category']
  list_filter = ['mapping_activity_category', 'mapping_activity_sub_category', 'mongo_sub_category', 'status']

    
  class Meta:
    model = MappingSubCategory
