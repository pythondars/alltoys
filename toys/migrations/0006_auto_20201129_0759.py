# Generated by Django 3.1.3 on 2020-11-29 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0005_auto_20201125_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='toy',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]