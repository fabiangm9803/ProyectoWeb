# Generated by Django 4.2.1 on 2023-06-24 01:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_venta_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.BigIntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='venta',
            name='estado',
        ),
        migrations.AlterField(
            model_name='producto',
            name='oferta',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 21, 29, 54, 941282)),
        ),
        migrations.DeleteModel(
            name='Detalle',
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.venta'),
        ),
    ]
