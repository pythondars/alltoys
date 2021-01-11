# Generated by Django 3.1.3 on 2021-01-10 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0013_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='toy',
            name='is_for_boys',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='toy',
            name='is_free',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='toy',
            name='is_new',
            field=models.BooleanField(default=True),
        ),
    ]