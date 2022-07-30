from django.contrib import admin
from package.models import Package, PackagePrice, UserPackage
# Register your models here.


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):

  list_display = ['name', 'status']
  list_filter = ['name', 'status']

    
  class Meta:
    model = Package



@admin.register(PackagePrice)
class PackagePriceAdmin(admin.ModelAdmin):

  list_display = ['package', 'days', 'price']
  list_filter = ['package']

    
  class Meta:
    model = PackagePrice



@admin.register(UserPackage)
class UserPackageAdmin(admin.ModelAdmin):

  list_display = ['user', 'package', 'expired_at']
  list_filter = ['expired_at']

    
  class Meta:
    model = UserPackage
