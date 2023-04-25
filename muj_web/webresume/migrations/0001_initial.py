# Generated by Django 4.1.7 on 2023-04-11 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PracovniZkusenost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pozice', models.CharField(max_length=100)),
                ('zamestnavatel', models.CharField(max_length=100)),
                ('doba', models.CharField(max_length=150)),
                ('napln', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Projekt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=150)),
                ('urceni', models.CharField(max_length=150)),
                ('detail', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Vzdelani',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instituce', models.CharField(max_length=250)),
                ('titul', models.CharField(max_length=100)),
                ('doba', models.CharField(max_length=150)),
                ('obor', models.CharField(max_length=100)),
                ('popis', models.CharField(max_length=500)),
            ],
        ),
    ]