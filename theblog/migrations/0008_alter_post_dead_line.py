# Generated by Django 4.2 on 2023-05-27 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("theblog", "0007_post_dead_line"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="dead_line",
            field=models.DateField(null=True),
        ),
    ]
