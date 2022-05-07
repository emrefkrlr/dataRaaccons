from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserType(models.IntegerChoices):
  
	ADMIN = 1
	COMPANY = 2
	OPERATION = 3
  
  
class Account(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  profile = models.SlugField(null=True, blank=True, verbose_name='Profil Adresi')
  phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Telefon Numarası')
  is_online = models.BooleanField(default=0, verbose_name='Online ?')
  user_type = models.IntegerField(choices=UserType.choices, verbose_name='Kullanıcı Tipi')

  class Meta:
    verbose_name = 'Hesap'
    verbose_name_plural = 'Kullanıcı Hesapları'

  def __str__(self):
  	return self.user.username
