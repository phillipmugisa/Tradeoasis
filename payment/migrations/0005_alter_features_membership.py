# Generated by Django 4.0.6 on 2022-08-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0004_rename_membershipplanfeature_features"),
    ]

    operations = [
        migrations.AlterField(
            model_name="features",
            name="membership",
            field=models.ManyToManyField(
                related_name="features", to="payment.membershipplan"
            ),
        ),
    ]
