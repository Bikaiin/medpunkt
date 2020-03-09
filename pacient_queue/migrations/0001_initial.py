# Generated by Django 3.0.4 on 2020-03-09 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True)),
                ('Position', models.CharField(max_length=100)),
                ('Subdivision', models.CharField(max_length=100)),
                ('WorkingСonditions', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PatientCard',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pacient_queue.Patient')),
                ('slug', models.SlugField(blank=True)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
    ]
