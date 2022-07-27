# Generated by Django 4.0.3 on 2022-06-29 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stats_api', '0011_remove_customframe_user_and_more'),
        ('custom_tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomColumn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceHolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom', models.BooleanField(default=False)),
                ('char', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('column', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stats_api.column')),
                ('custom_column', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='custom_tables.customcolumn')),
                ('expression', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_tables.expression')),
            ],
        ),
        migrations.CreateModel(
            name='CustomColumnInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('custom_column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_tables.customcolumn')),
                ('custom_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_tables.customtable')),
            ],
        ),
        migrations.AddField(
            model_name='customcolumn',
            name='custom_table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_tables.customtable'),
        ),
        migrations.AddField(
            model_name='customcolumn',
            name='expression',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_tables.expression'),
        ),
        migrations.CreateModel(
            name='ColumnInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats_api.column')),
                ('custom_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_tables.customtable')),
            ],
        ),
        migrations.AddConstraint(
            model_name='placeholder',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('custom_column__isnull', False), ('custom', True)), models.Q(('column__isnull', False), ('custom', False)), _connector='OR'), name='custom or column'),
        ),
    ]
