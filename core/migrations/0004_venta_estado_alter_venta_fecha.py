# Generated by Django 4.1.5 on 2023-06-13 19:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_venta_detalle"),
    ]

    operations = [
        migrations.AddField(
            model_name="venta",
            name="estado",
            field=models.CharField(default="EN PREPARACION", max_length=20),
        ),
        migrations.AlterField(
            model_name="venta",
            name="fecha",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 6, 13, 19, 59, 58, 745063, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]