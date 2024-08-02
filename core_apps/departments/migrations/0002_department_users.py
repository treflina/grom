# Generated by Django 5.0.7 on 2024-07-31 17:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("departments", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="department",
            name="users",
            field=models.ManyToManyField(
                related_name="departments", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
