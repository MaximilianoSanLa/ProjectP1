# Generated by Django 5.0.1 on 2024-03-18 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client_User', '0005_vet_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='comment',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]