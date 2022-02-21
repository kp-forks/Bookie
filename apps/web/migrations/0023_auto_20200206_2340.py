# Generated by Django 2.2.8 on 2020-02-06 22:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0022_profile_activation_code"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="activation_code",
        ),
        migrations.CreateModel(
            name="ActivationTokens",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.UUIDField(default=uuid.uuid4)),
                ("created", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.Profile"
                    ),
                ),
            ],
        ),
    ]
