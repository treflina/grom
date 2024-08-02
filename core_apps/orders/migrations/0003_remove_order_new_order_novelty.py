# Generated by Django 5.0.7 on 2024-08-01 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_order_created_by"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="new",
        ),
        migrations.AddField(
            model_name="order",
            name="novelty",
            field=models.BooleanField(default=False, verbose_name="novelty"),
        ),
    ]
