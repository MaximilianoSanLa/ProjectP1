# Generated by Django 5.0.1 on 2024-05-17 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client_User', '0002_remove_log_in_password_remove_log_in_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vet',
            name='average_score',
            field=models.IntegerField(null=True),
        ),
    ]