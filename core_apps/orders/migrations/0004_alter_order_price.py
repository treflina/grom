# Generated by Django 5.0.7 on 2024-08-01 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0003_remove_order_new_order_novelty"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="price",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=7, verbose_name="price"
            ),
        ),
    ]
