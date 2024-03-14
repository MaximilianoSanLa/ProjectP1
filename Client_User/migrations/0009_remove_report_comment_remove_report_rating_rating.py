# Generated by Django 5.0.1 on 2024-03-13 21:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client_User', '0008_alter_report_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='report',
            name='rating',
        ),
        migrations.CreateModel(
            name='rating',
            fields=[
                ('rating_id', models.IntegerField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=100, null=True)),
                ('rating', models.IntegerField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client_User.client')),
                ('vet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client_User.vet')),
            ],
        ),
    ]
