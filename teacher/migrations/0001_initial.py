# Generated by Django 5.1 on 2024-09-10 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
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
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("birthday", models.DateField()),
                ("phone_number", models.CharField(max_length=10)),
                ("url_picture", models.URLField()),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("MALE", "Male"),
                            ("FEMALE", "Female"),
                            ("OTHER", "Other"),
                        ],
                        max_length=6,
                    ),
                ),
                ("available", models.BooleanField()),
                ("speciality", models.CharField(max_length=100)),
                (
                    "address",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.address",
                    ),
                ),
            ],
            options={
                "verbose_name": "Teacher",
                "verbose_name_plural": "Teachers",
            },
        ),
    ]
