# Generated by Django 3.1.3 on 2020-11-17 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0026_auto_20201117_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='cont_approved',
        ),
        migrations.AddField(
            model_name='case',
            name='cont_consent',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
