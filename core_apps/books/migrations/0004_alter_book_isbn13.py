# Generated by Django 5.0.7 on 2024-08-01 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0003_remove_book_author_book_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="isbn13",
            field=models.BigIntegerField(
                blank=True, null=True, unique=True, verbose_name="ISBN13"
            ),
        ),
    ]
