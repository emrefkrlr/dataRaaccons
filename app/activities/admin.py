from django.contrib import admin
from activities.models import Activities, ActivityCategory

# Register your models here.


@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):

  list_display = ['name', 'status']
  list_filter = ['name', 'status']

    
  class Meta:
    model = Activities


@admin.register(ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):

  list_display = ['name', 'status']
  list_filter = ['name', 'status']

    
  class Meta:
    model = ActivityCategory
