# Generated by Django 4.0.6 on 2022-08-23 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0002_discussion_discussionreply"),
    ]

    operations = [
        migrations.AddField(
            model_name="discussionreply",
            name="description",
            field=models.TextField(default="rr", verbose_name="Description"),
            preserve_default=False,
        ),
    ]
