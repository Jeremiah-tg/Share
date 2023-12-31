# Generated by Django 4.2 on 2023-04-25 21:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("theblog", "0003_post_title_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="post_date",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="title_link",
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name="post",
            name="title_tag",
            field=models.CharField(max_length=255),
        ),
    ]
