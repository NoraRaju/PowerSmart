# Generated by Django 4.2.1 on 2023-05-25 04:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_mgmt', '0005_alter_login_dob_alter_login_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='DOB',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
