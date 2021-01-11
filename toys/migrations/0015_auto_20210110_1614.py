# Generated by Django 3.1.3 on 2021-01-10 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0014_auto_20210110_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toy',
            name='is_for_boys',
        ),
        migrations.AddField(
            model_name='toy',
            name='gender_of_players',
            field=models.CharField(blank=True, choices=[('boys', 'Boys'), ('girls', 'Girls')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='toy',
            name='type',
            field=models.CharField(blank=True, choices=[('animals', 'Animals'), ('dolls', 'Dolls'), ('cars', 'Cars'), ('educational_toys', 'Educational Toys'), ('electronic_toys', 'Electronic Toys'), ('other', 'Other')], max_length=16, null=True),
        ),
    ]