# Generated by Django 5.0.7 on 2024-08-01 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0004_alter_order_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="amount",
            field=models.PositiveSmallIntegerField(
                default=1, verbose_name="amount"
            ),
        ),
    ]
