# Generated by Django 3.1.3 on 2020-11-17 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0024_auto_20201117_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='cont_approved',
            field=models.BooleanField(blank=True, default='Unresponded', null=True),
        ),
    ]