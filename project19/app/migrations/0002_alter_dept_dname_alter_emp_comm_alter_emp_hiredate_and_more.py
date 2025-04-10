# Generated by Django 4.1 on 2025-03-06 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dept",
            name="dname",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="emp",
            name="comm",
            field=models.DecimalField(
                blank=True, decimal_places=3, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="emp",
            name="hiredate",
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="emp",
            name="mgr",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app.emp",
            ),
        ),
        migrations.AlterField(
            model_name="emp",
            name="sal",
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
