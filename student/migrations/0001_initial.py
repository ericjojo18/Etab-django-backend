# Generated by Django 5.1 on 2024-08-28 09:08

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
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("city", models.CharField(max_length=100)),
                ("birth_date", models.DateField()),
                ("phone", models.CharField(max_length=10)),
                ("classrom", models.CharField(max_length=10)),
                ("registration_number", models.CharField(max_length=30)),
                ("slug", models.SlugField(blank=True)),
            ],
            options={
                "verbose_name": "Student",
                "verbose_name_plural": "Students",
            },
        ),
    ]
