# Generated by Django 4.1.6 on 2023-03-22 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0013_alter_post_options_alter_post_post_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="post_image",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]
