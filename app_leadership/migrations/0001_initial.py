# Generated by Django 5.0.4 on 2024-05-10 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leadership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leader_full_name', models.CharField(max_length=100)),
                ('leader_position', models.CharField(max_length=100)),
                ('leader_email', models.CharField(max_length=100)),
                ('leader_phone_number', models.CharField(max_length=100)),
                ('leader_Works_days', models.CharField(max_length=100)),
                ('leader_spessionality', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Leadership',
                'db_table': 'leadership',
            },
        ),
        migrations.CreateModel(
            name='StructuralUnits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=200)),
                ('boss_full_name', models.CharField(max_length=100)),
                ('boss_email', models.CharField(max_length=100)),
                ('boss_phone_number', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Structural Units',
                'verbose_name_plural': 'Structural Units',
                'db_table': 'structural_units',
            },
        ),
    ]
