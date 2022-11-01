# Generated by Django 4.1.2 on 2022-10-30 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0005_alter_grados_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtemasmateria',
            name='descripcionSubTema',
        ),
        migrations.RemoveField(
            model_name='subtemasmateria',
            name='linkSubTema',
        ),
        migrations.RemoveField(
            model_name='subtemasmateria',
            name='tituloSubTema',
        ),
        migrations.CreateModel(
            name='Recursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloRecursos', models.CharField(max_length=255)),
                ('descripcionRecursos', models.TextField(blank=True, null=True)),
                ('linkRecursos', models.URLField()),
                ('subTemasMateria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recursos.subtemasmateria')),
            ],
        ),
    ]