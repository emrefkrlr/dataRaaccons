from django.contrib import admin
from account.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.


class AccountLıne(admin.StackedInline):
  model = Account
  can_delete = False
  verbose_name_plural = 'Accounts'
    

class CustomizeUserAdmin(UserAdmin):
  inlines = (AccountLıne, )
    
admin.site.unregister(User)
admin.site.register(User, CustomizeUserAdmin)
admin.site.register(Account)

