# Generated by Django 5.0.7 on 2024-07-31 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=200, unique=True, verbose_name="name"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Publisher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=250, unique=True, verbose_name="publisher"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="book"),
                ),
                ("isbn13", models.BigIntegerField(unique=True)),
                (
                    "for_kids",
                    models.BooleanField(
                        default=False, verbose_name="for kids"
                    ),
                ),
                (
                    "textbook",
                    models.BooleanField(
                        default=False, verbose_name="textbook"
                    ),
                ),
                (
                    "author",
                    models.ManyToManyField(
                        related_name="authors", to="books.author"
                    ),
                ),
                (
                    "publisher",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="books.publisher",
                    ),
                ),
            ],
            options={
                "verbose_name": "Book",
                "verbose_name_plural": "Books",
                "ordering": ["author__name", "title"],
            },
        ),
    ]
