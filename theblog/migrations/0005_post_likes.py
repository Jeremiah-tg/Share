# Generated by Django 4.2 on 2023-05-04 20:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("theblog", "0004_post_post_date_alter_post_title_link_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                related_name="share_post", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
