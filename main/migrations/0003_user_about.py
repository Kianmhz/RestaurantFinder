# Generated by Django 4.2.1 on 2023-06-15 20:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_remove_review_username_review_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="about",
            field=models.TextField(blank=True, null=True),
        ),
    ]
