# Generated by Django 3.2.13 on 2022-06-17 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_usertype_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='form_company',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Form Company'),
        ),
    ]