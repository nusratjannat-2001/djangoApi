# Generated by Django 4.2.2 on 2023-06-22 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breed',
            name='friendliness',
        ),
        migrations.RemoveField(
            model_name='breed',
            name='size',
        ),
    ]
