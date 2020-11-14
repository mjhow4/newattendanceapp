# Generated by Django 3.1.3 on 2020-11-14 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0009_defense_case'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='continuance',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='defense_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='plea',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Defense',
        ),
    ]
