# Generated by Django 4.0.5 on 2022-06-28 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=30)),
                ('ap_paterno', models.CharField(max_length=30)),
                ('ap_materno', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('nombre_vacuna', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
