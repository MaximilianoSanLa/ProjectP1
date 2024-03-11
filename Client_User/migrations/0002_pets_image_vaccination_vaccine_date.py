# Generated by Django 5.0.1 on 2024-03-11 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client_User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='image',
            field=models.ImageField(default=1, upload_to='client/static/img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vaccination',
            name='vaccine_date',
            field=models.DateField(null=True),
        ),
    ]
