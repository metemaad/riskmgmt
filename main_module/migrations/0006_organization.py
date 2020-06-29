# Generated by Django 3.0.3 on 2020-06-27 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0005_auto_20200627_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('ris_appetite', models.TextField(blank=True)),
                ('ris_tolerance', models.TextField(blank=True)),
            ],
        ),
    ]
