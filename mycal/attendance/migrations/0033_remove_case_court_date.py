# Generated by Django 3.1.3 on 2020-11-19 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0032_auto_20201118_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='court_date',
        ),
    ]
