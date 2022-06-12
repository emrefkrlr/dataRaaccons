from django.contrib import admin
from companies.models import Companies, CompanyActivities
# Register your models here.

@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):

  list_display = ['name', 'status']
  list_filter = ['name', 'status']

    
  class Meta:
    model = Companies


@admin.register(CompanyActivities)
class CompanyActivitiesAdmin(admin.ModelAdmin):

  list_display = ['company', 'activity']
  list_filter = ['company', 'activity']

    
  class Meta:
    model = CompanyActivities

