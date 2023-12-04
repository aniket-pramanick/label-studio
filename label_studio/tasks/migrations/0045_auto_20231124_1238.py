# Generated by Django 3.2.20 on 2023-11-24 12:38

from django.db import migrations, models
from django.conf import settings

# Determine if using SQLite or PostgreSQL
IS_SQLITE = settings.DJANGO_DB == settings.DJANGO_DB_SQLITE

if IS_SQLITE:
    from django.db.migrations import AddIndex
else:
    from django.contrib.postgres.operations import AddIndexConcurrently as AddIndex


class Migration(migrations.Migration):
    atomic = IS_SQLITE

    dependencies = [
        ('tasks', '0044_auto_20230907_0155'),
    ]

    operations = [
        AddIndex(
            model_name='annotation',
            index=models.Index(fields=['project_id', 'completed_by_id'], name='task_compl_project_completed_by_idx'),
        ),
        AddIndex(
            model_name='annotation',
            index=models.Index(fields=['task_id', 'id'], name='task_compl_task_id_idx'),
        ),
    ]
