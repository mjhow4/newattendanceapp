# Generated by Django 3.1.3 on 2020-11-17 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0016_auto_20201117_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='plea_request',
            field=models.TextField(blank=True, default='none', max_length=200, null=True),
        ),
    ]