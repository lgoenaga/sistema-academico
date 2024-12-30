# Generated by Django 5.1.4 on 2024-12-28 21:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('codigo', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('identificacion', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('identificacion', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Submodulos',
            fields=[
                ('codigo', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateField(auto_now=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cursos')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.estudiantes')),
            ],
        ),
        migrations.AddField(
            model_name='cursos',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profesores'),
        ),
        migrations.AddField(
            model_name='estudiantes',
            name='submodulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.submodulos'),
        ),
        migrations.AddField(
            model_name='cursos',
            name='submodulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.submodulos'),
        ),
    ]
