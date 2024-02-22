# Generated by Django 5.0.1 on 2024-02-20 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log_in',
            fields=[
                ('log_id', models.IntegerField(default=-1, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='client',
            name='email',
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('reason_appointment', models.CharField(max_length=200, null=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.client')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='log_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hello.log_in'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Phone_Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_intials', models.CharField(max_length=4)),
                ('phone', models.CharField(max_length=15)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.client')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.IntegerField(primary_key=True, serialize=False)),
                ('test_findings', models.CharField(max_length=200, null=True)),
                ('diagnosis', models.CharField(max_length=200, null=True)),
                ('prescribed_treatment', models.CharField(max_length=200, null=True)),
                ('recommendations', models.CharField(max_length=200, null=True)),
                ('additional_note', models.CharField(max_length=200, null=True)),
                ('appointement_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.appointment')),
                ('medical_history_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.medical_history')),
            ],
        ),
        migrations.CreateModel(
            name='Vet',
            fields=[
                ('vet_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('country_intials', models.CharField(max_length=4)),
                ('phone', models.CharField(max_length=15)),
                ('log_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.log_in')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='vet_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.vet'),
        ),
    ]