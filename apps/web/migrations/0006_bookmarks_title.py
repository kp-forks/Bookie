# Generated by Django 2.1.5 on 2019-02-07 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0005_auto_20190207_2148"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookmarks",
            name="title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
