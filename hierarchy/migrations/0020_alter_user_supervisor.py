# Generated by Django 5.0.4 on 2024-04-19 13:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0019_rename_leader_approved_task_approved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supervised_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
