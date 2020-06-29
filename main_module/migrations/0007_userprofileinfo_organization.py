# Generated by Django 3.0.3 on 2020-06-27 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0006_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_module.Organization'),
        ),
    ]
