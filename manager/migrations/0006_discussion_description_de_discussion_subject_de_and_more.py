# Generated by Django 4.0.6 on 2022-08-24 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_discussion_description_ar_discussion_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='description_de',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='discussion',
            name='subject_de',
            field=models.CharField(max_length=256, null=True, verbose_name='Subject'),
        ),
        migrations.AddField(
            model_name='discussionreply',
            name='description_de',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='service',
            name='description_de',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='service',
            name='name_de',
            field=models.CharField(max_length=256, null=True, verbose_name='Name'),
        ),
    ]
