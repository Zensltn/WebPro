# Generated by Django 5.0.3 on 2024-06-19 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perkuliahan', '0004_rename_namalengkap_mahasiswa_namamahasiswa'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Dosen',
        ),
    ]