# Generated by Django 4.0.6 on 2022-08-16 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0002_alter_showroom_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="showroom",
            name="location",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="manager.location",
            ),
        ),
    ]