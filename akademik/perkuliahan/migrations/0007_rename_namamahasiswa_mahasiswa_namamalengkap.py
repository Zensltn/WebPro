# Generated by Django 5.0.3 on 2024-06-19 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perkuliahan', '0006_dosen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mahasiswa',
            old_name='namamahasiswa',
            new_name='namamalengkap',
        ),
    ]
