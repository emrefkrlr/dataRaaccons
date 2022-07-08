from django.db import models
from django.contrib.auth.models import User
from companies.models import Companies
from activities.models import Activities
# Create your models here.

class UserType(models.Model):

  name = models.CharField(max_length=255, null=True, blank=True, verbose_name='User Type')
  status = models.BooleanField(default=1)
  
  class Meta:
    verbose_name = 'User Type'
    verbose_name_plural = 'User Type'

  def __str__(self):
  	return self.name

class Account(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  profile = models.SlugField(null=True, blank=True, verbose_name='Profile')
  phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Phone Number')
  is_online = models.BooleanField(default=0, verbose_name='Online ?')
  user_type = models.ForeignKey(UserType, null=True, related_name='account_user_type', on_delete=models.CASCADE)
  form_company = models.CharField(max_length=255, null=True, blank=True, verbose_name='Form Company')
  verified = models.BooleanField(default=0, verbose_name=' Hesap Doğrulandı')
  verified_code = models.CharField(max_length=255, null=True, blank=True)

  class Meta:
    verbose_name = 'Account'
    verbose_name_plural = 'Account'

  def __str__(self):
  	return self.user.username


class AccountCompany(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account_company_user', null=True)
  company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='account_company_company', null=True)
  activity = models.ForeignKey(Activities, on_delete=models.CASCADE, related_name='account_company_activity', null=True)

  class Meta:
    verbose_name = 'Account Company Relations'
    verbose_name_plural = 'Account Company Relations'

  def __str__(self):
  	return self.user.username

## Sil ##
class PersonalUserActivity(models.Model):
  user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='personal_user_activity_user', null=True, limit_choices_to={"user_type": 2})
  activity = models.ForeignKey(Activities, on_delete=models.CASCADE, related_name='personal_user_activity_activity', null=True)

  class Meta:
    verbose_name = 'Personal User Activity'
    verbose_name_plural = 'Personal User Activity'

  def __str__(self):
  	return self.user
