# Generated by Django 3.0.3 on 2020-06-27 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0004_auto_20200627_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='riskcategory',
            name='type_of_category',
            field=models.CharField(choices=[('0', 'Pure Risk'), ('1', 'Speculative Risk')], default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='riskcategory',
            name='hierarcy',
            field=models.CharField(blank=True, default='', max_length=1024),
        ),
    ]
