# Generated by Django 4.1.7 on 2023-03-23 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_customuser_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_moderator',
            field=models.BooleanField(default=False),
        ),
    ]
