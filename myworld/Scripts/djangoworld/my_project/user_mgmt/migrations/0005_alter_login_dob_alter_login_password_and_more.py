# Generated by Django 4.2.1 on 2023-05-23 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_mgmt', '0004_alter_login_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='DOB',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='Password',
            field=models.TextField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='PhnNo',
            field=models.BigIntegerField(null=True),
        ),
    ]
