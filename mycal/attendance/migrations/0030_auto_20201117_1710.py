# Generated by Django 3.1.3 on 2020-11-17 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0029_auto_20201117_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='cont_consent',
            field=models.CharField(blank=True, default='Unresponded', max_length=12, null=True),
        ),
    ]
