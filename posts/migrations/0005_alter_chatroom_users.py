# Generated by Django 4.1.6 on 2023-03-07 07:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0004_remove_chatroom_users_chatroom_users"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatroom",
            name="users",
            field=models.ManyToManyField(
                related_name="chatrooms", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
