# Generated by Django 3.1.3 on 2020-12-04 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0009_auto_20201204_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toy',
            name='user',
        ),
    ]
