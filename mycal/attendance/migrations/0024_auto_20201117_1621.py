# Generated by Django 3.1.3 on 2020-11-17 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0023_auto_20201117_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='cont_approved',
            field=models.CharField(blank=True, default='Unresponded', max_length=50, null=True),
        ),
    ]