# Generated by Django 4.2.1 on 2023-05-21 18:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Test",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("password", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
            ],
        ),
    ]
