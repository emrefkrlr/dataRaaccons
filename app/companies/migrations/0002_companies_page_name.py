# Generated by Django 3.2.13 on 2022-06-28 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='page_name',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Company Page Name'),
        ),
    ]
