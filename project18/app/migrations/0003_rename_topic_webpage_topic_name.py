# Generated by Django 5.1.6 on 2025-03-12 05:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_webpage_email"),
    ]

    operations = [
        migrations.RenameField(
            model_name="webpage",
            old_name="topic",
            new_name="topic_name",
        ),
    ]
