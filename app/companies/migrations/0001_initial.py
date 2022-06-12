# Generated by Django 3.2.13 on 2022-05-02 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, blank=None, editable=False, null=True, verbose_name='Created Date')),
                ('name', models.CharField(blank=None, max_length=120, verbose_name='Company Name')),
                ('status', models.BooleanField(default=1)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Updated Date')),
            ],
            options={
                'verbose_name': 'Companies',
                'verbose_name_plural': 'Company',
            },
        ),
        migrations.CreateModel(
            name='CompanyActivities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True, blank=None, editable=False, null=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Updated Date')),
                ('activity', models.ForeignKey(null=None, on_delete=django.db.models.deletion.CASCADE, related_name='activities_name', to='activities.activities')),
                ('company', models.ForeignKey(null=None, on_delete=django.db.models.deletion.CASCADE, related_name='companyies_name', to='companies.companies')),
            ],
            options={
                'verbose_name': 'Company Activities',
                'verbose_name_plural': 'Company Activiy',
            },
        ),
    ]
