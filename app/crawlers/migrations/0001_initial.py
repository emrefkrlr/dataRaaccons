# Generated by Django 3.2.16 on 2022-10-10 15:53

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        ('demands', '0001_initial'),
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrawlerError',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crawler_id', models.IntegerField(blank=True, default=0, null=True, verbose_name='Crawler ID')),
                ('error_message', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
            ],
            options={
                'verbose_name': 'Crawler Err',
                'verbose_name_plural': 'Crawler Err',
            },
        ),
        migrations.CreateModel(
            name='WebDriverConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(blank=True, max_length=120, null=True, verbose_name='IP address')),
            ],
            options={
                'verbose_name': 'WebDriver',
                'verbose_name_plural': 'WebDriver',
            },
        ),
        migrations.CreateModel(
            name='CrawlersConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('css_selector', models.CharField(blank=True, max_length=120, null=True, verbose_name='Css Selector')),
                ('p1', models.CharField(blank=True, max_length=120, null=True, verbose_name='p1')),
                ('p2', models.CharField(blank=True, max_length=120, null=True, verbose_name='p2')),
                ('p3', models.CharField(blank=True, max_length=120, null=True, verbose_name='p3')),
                ('p4', models.CharField(blank=True, max_length=120, null=True, verbose_name='p4')),
                ('p5', models.CharField(blank=True, max_length=120, null=True, verbose_name='p5')),
                ('p6', models.CharField(blank=True, max_length=120, null=True, verbose_name='p6')),
                ('p7', models.CharField(blank=True, max_length=120, null=True, verbose_name='p7')),
                ('p8', models.CharField(blank=True, max_length=120, null=True, verbose_name='p8')),
                ('p9', models.CharField(blank=True, max_length=120, null=True, verbose_name='p9')),
                ('p10', models.CharField(blank=True, max_length=120, null=True, verbose_name='p10')),
                ('p11', models.CharField(blank=True, max_length=120, null=True, verbose_name='p11')),
                ('p12', models.CharField(blank=True, max_length=120, null=True, verbose_name='p12')),
                ('p13', models.CharField(blank=True, max_length=120, null=True, verbose_name='p13')),
                ('p14', models.CharField(blank=True, max_length=120, null=True, verbose_name='p14')),
                ('p15', models.CharField(blank=True, max_length=120, null=True, verbose_name='p15')),
                ('p16', models.CharField(blank=True, max_length=120, null=True, verbose_name='p16')),
                ('p17', models.CharField(blank=True, max_length=120, null=True, verbose_name='p17')),
                ('p18', models.CharField(blank=True, max_length=120, null=True, verbose_name='p18')),
                ('p19', models.CharField(blank=True, max_length=120, null=True, verbose_name='p19')),
                ('p20', models.CharField(blank=True, max_length=120, null=True, verbose_name='p20')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('activity', models.ForeignKey(null=None, on_delete=django.db.models.deletion.CASCADE, related_name='crawler_config_activitiy_name', to='activities.activities')),
                ('company', models.ForeignKey(null=None, on_delete=django.db.models.deletion.CASCADE, related_name='crawler_config_company_name', to='companies.companies')),
                ('demand', models.ForeignKey(null=None, on_delete=django.db.models.deletion.CASCADE, related_name='crawler_config_demands_name', to='demands.demands')),
            ],
            options={
                'verbose_name': 'Crawler Config',
                'verbose_name_plural': 'Crawler Config',
            },
        ),
        migrations.CreateModel(
            name='Crawlers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_url', models.CharField(blank=None, max_length=255, verbose_name='Page Url')),
                ('page_numbers', models.IntegerField(blank=True, default=0, null=True, verbose_name='Page Numbers')),
                ('page_name', models.CharField(blank=None, max_length=120, verbose_name='Page Name')),
                ('page_category', models.CharField(blank=True, max_length=120, null=True, verbose_name='Page Category')),
                ('css_selector', models.CharField(blank=True, max_length=120, null=True, verbose_name='Css Selector')),
                ('schedule', models.CharField(blank=True, max_length=120, null=True, verbose_name='Schedule Config')),
                ('status', models.BooleanField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Date')),
                ('activity', models.ForeignKey(null=None, on_delete=django.db.models.deletion.CASCADE, related_name='activitiy_name', to='activities.activities')),
                ('activity_category', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='activity', chained_model_field='activity', on_delete=django.db.models.deletion.CASCADE, to='activities.activitycategory')),
                ('company', models.ForeignKey(null=None, on_delete=django.db.models.deletion.CASCADE, related_name='company_name', to='companies.companies')),
                ('demand', models.ForeignKey(null=None, on_delete=django.db.models.deletion.CASCADE, related_name='demands_name', to='demands.demands')),
            ],
            options={
                'verbose_name': 'Crawlers',
                'verbose_name_plural': 'Crawler',
            },
        ),
    ]
