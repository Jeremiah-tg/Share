# Generated by Django 4.2 on 2023-05-25 18:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("theblog", "0005_post_likes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="body",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
