from django.contrib import admin
from account.models import Account, AccountCompany,UserType
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from account.models import AccountCompany


# Register your models here.


class AccountLıne(admin.StackedInline):
  model = Account
  can_delete = False
  verbose_name_plural = 'Accounts'

class AccountCompanyLıne(admin.StackedInline):
  model = AccountCompany
  can_delete = False
  verbose_name_plural = 'Company Info'
    

class CustomizeUserAdmin(UserAdmin):
  inlines = (AccountLıne, AccountCompanyLıne )
    
admin.site.unregister(User)
admin.site.register(User, CustomizeUserAdmin)
admin.site.register(Account)

@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):

  list_display = ['name', 'status']

  class Meta:
      model = UserType

