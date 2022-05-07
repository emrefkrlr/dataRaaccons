from django.contrib import admin
from demands.models import Demands

# Register your models here.

@admin.register(Demands)
class DemandsAdmin(admin.ModelAdmin):

  list_display = ['name', 'status']
  list_filter = ['name', 'status']

    
  class Meta:
    model = Demands
