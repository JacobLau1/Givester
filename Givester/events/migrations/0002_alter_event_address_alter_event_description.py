# Generated by Django 4.2.7 on 2023-11-18 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=400),
        ),
    ]
