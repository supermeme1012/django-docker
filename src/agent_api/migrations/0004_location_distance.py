# Generated by Django 3.1.8 on 2023-04-10 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent_api', '0003_auto_20230409_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='distance',
            field=models.FloatField(default=0.0),
        ),
    ]
