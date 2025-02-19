# Generated by Django 3.2.25 on 2024-10-15 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20241013_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='horarioclase',
            name='docente_materia_grado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.docentemateriagrado'),
        ),
        migrations.AlterUniqueTogether(
            name='horarioclase',
            unique_together={('docente_materia_grado', 'dia_semana', 'hora_inicio', 'hora_fin')},
        ),
        migrations.RemoveField(
            model_name='horarioclase',
            name='docente',
        ),
        migrations.RemoveField(
            model_name='horarioclase',
            name='materia',
        ),
    ]
