# Generated by Django 3.2.4 on 2021-09-04 04:59

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('regular', 'Regular'), ('square', 'Square')], max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('topping', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=40), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaTopping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(max_length=40, unique=True)),
            ],
        ),
    ]