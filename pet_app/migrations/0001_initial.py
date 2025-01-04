# Generated by Django 4.2.16 on 2024-12-21 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
            ],
            options={"db_table": "blog",},
        ),
        migrations.CreateModel(
            name="Pet",
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
                ("petName", models.CharField(max_length=255)),
                ("petAge", models.IntegerField()),
                ("petBreed", models.CharField(max_length=255)),
                ("petImage", models.CharField(max_length=500)),
            ],
            options={"db_table": "pets",},
        ),
    ]
