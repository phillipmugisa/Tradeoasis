# Generated by Django 4.0.6 on 2022-09-05 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0012_remove_chatroom_chatfile_chatroom_chatfilepath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
