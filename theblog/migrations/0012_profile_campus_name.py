# Generated by Django 4.2 on 2023-06-03 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("theblog", "0011_profile_facebook_url_profile_linkedin_url_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="campus_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]