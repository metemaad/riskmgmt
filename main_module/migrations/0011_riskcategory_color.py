# Generated by Django 3.0.3 on 2020-06-27 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0010_auto_20200627_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='riskcategory',
            name='color',
            field=models.CharField(blank=True, default='#FFFFFF', max_length=10, null=True),
        ),
    ]