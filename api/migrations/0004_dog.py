# Generated by Django 4.2.2 on 2023-06-22 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_breed_exerciseneeds_breed_friendliness_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('None', 'None')], max_length=20)),
                ('color', models.CharField(max_length=30)),
                ('favorite_food', models.CharField(max_length=40)),
                ('favorite_toy', models.CharField(max_length=30)),
                ('breed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.breed')),
            ],
        ),
    ]