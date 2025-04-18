# Generated by Django 5.1.6 on 2025-04-18 06:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                    "stname",
                    models.CharField(
                        max_length=100,
                        validators=[django.core.validators.MinLengthValidator(5)],
                    ),
                ),
                ("stage", models.IntegerField()),
                ("stemail", models.EmailField(max_length=254)),
                (
                    "stmobile",
                    models.CharField(
                        max_length=10,
                        validators=[
                            django.core.validators.RegexValidator("[6-9]\\d{9}")
                        ],
                    ),
                ),
            ],
        ),
    ]
