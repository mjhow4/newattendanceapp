# Generated by Django 3.1.3 on 2020-11-17 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0019_auto_20201117_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='continuance',
            field=models.DateField(blank=True, default='Unrequested', null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='defense_name',
            field=models.CharField(blank=True, default='Undeclared', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='disposition',
            field=models.TextField(blank=True, default='Unresolved', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='plea_request',
            field=models.TextField(blank=True, default='Unrequested', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='response_by',
            field=models.TextField(blank=True, default='Unresponded', max_length=200, null=True),
        ),
    ]
