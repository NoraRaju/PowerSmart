# Generated by Django 4.2.1 on 2023-05-23 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='Age',
            field=models.IntegerField(default=0),
        ),
    ]