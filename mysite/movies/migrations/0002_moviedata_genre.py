# Generated by Django 5.2 on 2025-05-06 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='genre',
            field=models.CharField(default='action', max_length=100),
        ),
    ]
