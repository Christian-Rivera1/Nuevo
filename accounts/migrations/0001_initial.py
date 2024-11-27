# Generated by Django 3.2.25 on 2024-09-15 16:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('dui', models.CharField(max_length=9, primary_key=True, serialize=False, unique=True)),
                ('nombreDocente', models.CharField(max_length=100)),
                ('apellidoDocente', models.CharField(max_length=100)),
                ('generoDocente', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('direccionDocente', models.CharField(max_length=100)),
                ('correoDocente', models.EmailField(max_length=254, unique=True)),
                ('fechaRegistroDocente', models.DateField(auto_now_add=True)),
                ('edadDocente', models.IntegerField()),
                ('telefonoDocente', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^\\d{8}$', 'Ingrese un número de teléfono válido de 8 dígitos.')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('idGrado', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombreGrado', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='GradoSeccion',
            fields=[
                ('id_gradoseccion', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grado_secciones', to='accounts.grado')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id_materia', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_materia', models.CharField(max_length=25)),
                ('anio_materia', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('idSeccion', models.AutoField(primary_key=True, serialize=False)),
                ('nombreSeccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoActividad',
            fields=[
                ('id_tipoactividad', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombretipoactividad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MateriaGradoSeccion',
            fields=[
                ('id_matrgrasec', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('id_gradoseccion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='accounts.gradoseccion')),
                ('id_materia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='accounts.materia')),
            ],
        ),
        migrations.AddField(
            model_name='gradoseccion',
            name='seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grado_secciones', to='accounts.seccion'),
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id_alumno', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombreAlumno', models.CharField(max_length=100)),
                ('apellidoAlumno', models.CharField(max_length=100)),
                ('edadAlumno', models.IntegerField()),
                ('numeroTelefonoAlumno', models.CharField(max_length=8)),
                ('fechaRegistroAlumno', models.DateField(auto_now_add=True)),
                ('nombreResponsable', models.CharField(max_length=100)),
                ('apellidoResposable', models.CharField(max_length=100)),
                ('numeroTelefonoResposable', models.CharField(max_length=8)),
                ('duiResponsable', models.CharField(max_length=9, unique=True)),
                ('direccionResponsable', models.CharField(max_length=100)),
                ('edadResponsable', models.IntegerField()),
                ('id_gradoseccion', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounts.gradoseccion')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DocenteMateriaGrado',
            fields=[
                ('id_doc_mat_grado', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('dui', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='accounts.docente')),
                ('id_matrgrasec', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounts.materiagradoseccion')),
            ],
        ),
        migrations.CreateModel(
            name='Conducta',
            fields=[
                ('id_conducta', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('fecha_conducta', models.CharField(max_length=15)),
                ('obsevacion_conducta', models.CharField(max_length=250)),
                ('nota_conducta', models.FloatField()),
                ('id_alumno', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounts.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id_asistencia', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('fechaasistencia', models.DateField()),
                ('asistio', models.CharField(max_length=1)),
                ('id_alumno', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounts.estudiante')),
                ('idgradoseccion', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounts.gradoseccion')),
            ],
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignaciones', to='accounts.docente')),
                ('grado_seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignaciones', to='accounts.gradoseccion')),
            ],
        ),
        migrations.CreateModel(
            name='ActividadAcademica',
            fields=[
                ('id_actividad', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre_actividad', models.CharField(max_length=25)),
                ('descripcion_actividad', models.CharField(max_length=50)),
                ('fecha_actividad', models.DateField()),
                ('nota', models.FloatField()),
                ('id_alumno', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounts.estudiante')),
                ('id_matrgrasec', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounts.materiagradoseccion')),
                ('id_tipoactividad', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='accounts.tipoactividad', unique=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='gradoseccion',
            unique_together={('grado', 'seccion')},
        ),
    ]
