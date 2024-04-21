# Generated by Django 5.0.4 on 2024-04-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0017_delete_approve_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='is_approved',
            new_name='Leader_approved',
        ),
        migrations.AddField(
            model_name='task',
            name='Manager_approved',
            field=models.BooleanField(default=False),
        ),
    ]