# Generated by Django 3.1.3 on 2020-11-17 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0013_auto_20201115_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='attorney',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
