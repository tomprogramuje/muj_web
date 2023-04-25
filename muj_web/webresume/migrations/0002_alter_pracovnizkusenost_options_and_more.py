# Generated by Django 4.1.7 on 2023-04-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webresume', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pracovnizkusenost',
            options={'verbose_name': 'Pracovní zkušenost', 'verbose_name_plural': 'Pracovní zkušenosti'},
        ),
        migrations.AlterModelOptions(
            name='projekt',
            options={'verbose_name': 'Projekt', 'verbose_name_plural': 'Projekty'},
        ),
        migrations.AlterModelOptions(
            name='vzdelani',
            options={'verbose_name': 'Vzdělání', 'verbose_name_plural': 'Vzdělání'},
        ),
        migrations.AddField(
            model_name='projekt',
            name='doba',
            field=models.CharField(default='Únor 2023', max_length=150),
        ),
    ]
