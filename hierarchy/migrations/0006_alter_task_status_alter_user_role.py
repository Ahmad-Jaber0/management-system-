# Generated by Django 5.0.4 on 2024-04-14 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0005_user_supervisor_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('In Progress', 'In Progress'), ('Ready for test', 'Ready for test'), ('Completed', 'Completed')], max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Manager', 'Manager'), ('Team Leader', 'Team Leader'), ('Developer', 'Developer')], max_length=20),
        ),
    ]
