# Generated by Django 5.0.4 on 2024-06-27 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto_created_producto_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
