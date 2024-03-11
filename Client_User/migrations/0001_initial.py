# Generated by Django 5.0.1 on 2024-03-07 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log_in',
            fields=[
                ('log_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccines',
            fields=[
                ('vaccine_id', models.IntegerField(primary_key=True, serialize=False)),
                ('vaccine_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('log_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client_User.log_in')),
            ],
        ),
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('pet_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('race', models.CharField(max_length=100)),
                ('birth_date', models.DateField(max_length=99)),
                ('gender', models.BooleanField()),
                ('allergies', models.CharField(max_length=100)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client_User.client')),
            ],
        ),
        migrations.CreateModel(
            name='Medical_history',
            fields=[
                ('Medical_history_id', models.IntegerField(primary_key=True, serialize=False)),
                ('pet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client_User.pets')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('reason_appointment', models.CharField(max_length=200, null=True)),
                ('pet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client_User.pets')),
            ],
        ),
        migrations.CreateModel(
            name='Phone_Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_intials', models.CharField(max_length=4)),
                ('phone', models.CharField(max_length=15)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client_User.client')),
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
                ('update_note', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('appointement_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client_User.appointment')),
                ('medical_history_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client_User.medical_history')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='medical/file/')),
                ('report_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client_User.report')),
            ],
        ),
        migrations.CreateModel(
            name='Vaccination',
            fields=[
                ('vaccination_id', models.IntegerField(primary_key=True, serialize=False)),
                ('medical_history_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client_User.medical_history')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client_User.vaccines')),
            ],
        ),
        migrations.CreateModel(
            name='Vet',
            fields=[
                ('vet_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('country_intials', models.CharField(max_length=4)),
                ('phone', models.CharField(max_length=15)),
                ('log_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client_User.log_in')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='vet_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client_User.vet'),
        ),
    ]
