# Generated by Django 5.0.4 on 2024-05-10 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_movie_actors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(null=True, to='cinema.actor', verbose_name='Актер'),
        ),
    ]
