# Generated by Django 5.1.6 on 2025-05-19 06:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Emp",
            fields=[
                ("ename", models.CharField(max_length=100)),
                ("empno", models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
