# Generated by Django 3.0.3 on 2020-06-27 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0008_riskresiduals'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Loss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='LossIncident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_incident', to='main_module.Incident')),
                ('loss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cause_loss', to='main_module.Loss')),
            ],
        ),
        migrations.CreateModel(
            name='IncidentIssues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cause_incident', to='main_module.Incident')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_issue', to='main_module.Issue')),
            ],
        ),
    ]