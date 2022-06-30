# Generated by Django 4.0.5 on 2022-06-29 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_sis_vacuna', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_vacuna', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameModel(
            old_name='Usuario',
            new_name='Persona',
        ),
        migrations.CreateModel(
            name='Vacunacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosis', models.CharField(choices=[('primera_docis', 'Primera Docis'), ('segunda_docis', 'Segunda Docis'), ('tercera_docis', 'Tercera Docis'), ('cuarta_docis', 'Cuarta Docis')], default='primera_docis', max_length=30)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sis_vacuna.persona')),
                ('vacuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sis_vacuna.vacuna')),
            ],
        ),
    ]