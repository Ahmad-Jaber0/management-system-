# Generated by Django 5.0.4 on 2024-04-18 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0018_rename_is_approved_task_leader_approved_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Leader_approved',
            new_name='approved',
        ),
        migrations.RemoveField(
            model_name='task',
            name='Manager_approved',
        ),
    ]