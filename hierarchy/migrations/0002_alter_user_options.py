# Generated by Django 5.0.4 on 2024-04-12 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'managed': False},
        ),
    ]