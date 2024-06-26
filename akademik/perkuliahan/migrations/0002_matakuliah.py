# Generated by Django 5.0.3 on 2024-04-23 15:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perkuliahan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='matakuliah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodemk', models.CharField(max_length=100, verbose_name='Kode Matakuliah')),
                ('manamk', models.CharField(max_length=150, verbose_name='Nama Matakuliah')),
                ('semester', models.CharField(max_length=50, verbose_name='Semester')),
                ('Sks', models.IntegerField(verbose_name='SKS')),
                ('jurusan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perkuliahan.jurusan')),
            ],
        ),
    ]
