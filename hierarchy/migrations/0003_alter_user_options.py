# Generated by Django 5.0.4 on 2024-04-12 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
