from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Package(models.Model):

    name = models.CharField(max_length=255, null=None, blank=False, verbose_name='Package Name')
    package_detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created Date', editable=False, null=None, blank=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated Date', editable=False, null=None, blank=False)
    status = models.BooleanField(default=1)

    class Meta:
        verbose_name = 'Package'
        verbose_name_plural = 'Package'
	

    def __str__(self):
        return "%s" % self.name


class PackagePrice(models.Model):
    
    package = models.ForeignKey(Package, null=None, related_name='package_price_package', on_delete=models.CASCADE)
    days = models.IntegerField(default= 30, null=None, blank=False, verbose_name='Days')
    price = models.IntegerField(default= 0, null=None, blank=False, verbose_name='False')


    class Meta:
        verbose_name = 'PackagePrice'
        verbose_name_plural = 'PackagePrice'
	

    def __str__(self):
        return "%s" % self.package



class UserPackage(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, null=None, related_name='user_package_package', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created Date', editable=False, null=None, blank=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated Date', editable=False, null=None, blank=False)
    expired_at = models.DateTimeField(auto_now=False, editable=True, verbose_name='Expire Date', null=True, blank=True)

    class Meta:
        verbose_name = 'User Package'
        verbose_name_plural = 'User Package'
	

    def __str__(self):
        return "%s" % self.user.email




