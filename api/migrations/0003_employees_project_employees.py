# Generated by Django 5.1.2 on 2024-10-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_projectmanager_project_projectmanager"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employees",
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
                ("name", models.CharField(max_length=50, unique=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name="project",
            name="employees",
            field=models.ManyToManyField(to="api.employees"),
        ),
    ]
