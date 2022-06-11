# Generated by Django 4.0.3 on 2022-04-09 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stats_api', '0005_alter_column_frame'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomColumnType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomFrame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_custom_frames', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_frame', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='frame_players', to='stats_api.customframe')),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_custom_players', to='stats_api.player')),
            ],
        ),
        migrations.CreateModel(
            name='CustomColumnDef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='column_custom_columns', to='stats_api.column')),
                ('custom_column', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom_column_columns', to='stats_api.column')),
            ],
        ),
        migrations.CreateModel(
            name='CustomColumn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_id', models.CharField(max_length=100)),
                ('column_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom_column_type_columns', to='stats_api.customcolumntype')),
                ('custom_frame', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='frame_columns', to='stats_api.customframe')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
