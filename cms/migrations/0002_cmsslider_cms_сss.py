# Generated by Django 3.2.9 on 2021-11-08 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsslider',
            name='cms_сss',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='CSS класс'),
        ),
    ]
