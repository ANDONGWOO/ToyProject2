# Generated by Django 3.2.13 on 2023-05-24 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stopwatch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='user',
        ),
    ]