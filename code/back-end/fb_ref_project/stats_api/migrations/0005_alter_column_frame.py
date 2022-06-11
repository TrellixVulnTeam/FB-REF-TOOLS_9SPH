# Generated by Django 4.0.3 on 2022-03-30 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats_api', '0004_rename_records_added_frame_cols_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='frame',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='frame_columns', to='stats_api.frame'),
        ),
    ]
