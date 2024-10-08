# Generated by Django 5.1 on 2024-09-10 23:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AppSetting",
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
                ("smtp_server", models.CharField(max_length=200)),
                ("smtp_port", models.CharField(max_length=200)),
                ("smtp_username", models.CharField(max_length=200)),
                ("smtp_password", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "AppSetting",
                "verbose_name_plural": "AppSettings",
            },
        ),
        migrations.CreateModel(
            name="School",
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
                ("url_logo", models.URLField()),
                (
                    "app",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="school_app_id",
                        to="school.appsetting",
                    ),
                ),
            ],
            options={
                "verbose_name": "School",
                "verbose_name_plural": "Schools",
            },
        ),
    ]
