# Generated by Django 4.2.3 on 2023-07-27 15:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="resume",
            name="institute",
            field=models.CharField(default="institute", max_length=100),
        ),
        migrations.AddField(
            model_name="resume",
            name="qualification",
            field=models.CharField(default="Btech", max_length=100),
        ),
    ]