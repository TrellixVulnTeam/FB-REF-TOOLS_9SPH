# Generated by Django 4.0.3 on 2022-06-29 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats_api', '0009_alter_player_player_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
