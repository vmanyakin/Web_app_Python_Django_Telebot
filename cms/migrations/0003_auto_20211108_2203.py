# Generated by Django 3.2.9 on 2021-11-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_cmsslider_cms_сss'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cmsslider',
            name='cms_сss',
        ),
        migrations.AddField(
            model_name='cmsslider',
            name='cms_css',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='Текст'),
        ),
    ]
