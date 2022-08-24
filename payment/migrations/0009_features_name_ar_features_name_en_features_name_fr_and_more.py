# Generated by Django 4.0.6 on 2022-08-24 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_membershipreceipt_reference_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='features',
            name='name_ar',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='features',
            name='name_en',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='features',
            name='name_fr',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='membershipplan',
            name='currency_ar',
            field=models.CharField(max_length=6, null=True, verbose_name='Currency'),
        ),
        migrations.AddField(
            model_name='membershipplan',
            name='currency_en',
            field=models.CharField(max_length=6, null=True, verbose_name='Currency'),
        ),
        migrations.AddField(
            model_name='membershipplan',
            name='currency_fr',
            field=models.CharField(max_length=6, null=True, verbose_name='Currency'),
        ),
        migrations.AddField(
            model_name='membershipplan',
            name='description_ar',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='membershipplan',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='membershipplan',
            name='description_fr',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='membershipplan',
            name='name_ar',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='membershipplan',
            name='name_en',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='membershipplan',
            name='name_fr',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='membershipplan',
            name='price_ar',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Price'),
        ),
        migrations.AddField(
            model_name='membershipplan',
            name='price_en',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Price'),
        ),
        migrations.AddField(
            model_name='membershipplan',
            name='price_fr',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Price'),
        ),
        migrations.AddField(
            model_name='modeofpayment',
            name='name_ar',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='modeofpayment',
            name='name_en',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='modeofpayment',
            name='name_fr',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
        ),
    ]
