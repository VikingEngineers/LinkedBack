# Generated by Django 4.2.1 on 2023-05-12 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lm_projects', '0002_alter_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
