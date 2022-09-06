# Generated by Django 4.0.6 on 2022-09-02 18:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_showroom_name_ar_showroom_name_de_showroom_name_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=256, verbose_name='Country')),
                ('city', models.CharField(max_length=256, verbose_name='City')),
                ('view', models.CharField(max_length=256, verbose_name='View')),
                ('request_method', models.CharField(max_length=256, verbose_name='Request Method')),
                ('device', models.CharField(max_length=256, verbose_name='Device')),
                ('user_os', models.CharField(max_length=256, verbose_name='User Os')),
                ('created_on', models.DateField(default=django.utils.timezone.now, verbose_name='Created on')),
            ],
        ),
    ]
