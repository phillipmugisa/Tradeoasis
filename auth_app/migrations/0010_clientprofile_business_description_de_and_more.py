# Generated by Django 4.0.6 on 2022-08-24 04:38

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0009_clientprofile_business_description_ar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='business_description_de',
            field=models.TextField(null=True, verbose_name='Business Description'),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='business_name_de',
            field=models.CharField(max_length=256, null=True, verbose_name='Business Name'),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='city_de',
            field=models.CharField(max_length=256, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='country_code_de',
            field=models.CharField(max_length=20, null=True, verbose_name='Country Code'),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='country_de',
            field=models.CharField(max_length=256, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='mobile_user_de',
            field=models.CharField(max_length=20, null=True, verbose_name='Number'),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name_de',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name_de',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='user',
            name='username_de',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, null=True, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
