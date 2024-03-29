# Generated by Django 3.2.16 on 2022-10-10 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=None, verbose_name='Package Name')),
                ('package_detail', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=None, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, null=None, verbose_name='Updated Date')),
                ('status', models.BooleanField(default=1)),
            ],
            options={
                'verbose_name': 'Package',
                'verbose_name_plural': 'Package',
            },
        ),
        migrations.CreateModel(
            name='UserPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=None, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, null=None, verbose_name='Updated Date')),
                ('expired_at', models.DateTimeField(blank=True, null=True, verbose_name='Expire Date')),
                ('package', models.ForeignKey(null=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_package_package', to='package.package')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Package',
                'verbose_name_plural': 'User Package',
            },
        ),
        migrations.CreateModel(
            name='PackagePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.IntegerField(default=30, null=None, verbose_name='Days')),
                ('price', models.IntegerField(default=0, null=None, verbose_name='Price')),
                ('package', models.ForeignKey(null=None, on_delete=django.db.models.deletion.CASCADE, related_name='package_price_package', to='package.package')),
            ],
            options={
                'verbose_name': 'PackagePrice',
                'verbose_name_plural': 'PackagePrice',
            },
        ),
    ]
