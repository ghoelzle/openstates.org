# Generated by Django 2.2.3 on 2020-01-29 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0006_auto_20200129_2023"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="subscription_emails_html",
            field=models.BooleanField(default=True),
        ),
    ]