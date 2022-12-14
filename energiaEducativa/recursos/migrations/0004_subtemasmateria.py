# Generated by Django 4.1.2 on 2022-10-30 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0003_temasmaterias'),
    ]

    operations = [
        migrations.CreateModel(
            name='subTemasMateria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomSubTema', models.CharField(max_length=255)),
                ('tituloSubTema', models.CharField(max_length=255)),
                ('descripcionSubTema', models.TextField()),
                ('linkSubTema', models.URLField()),
                ('temasMateria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recursos.temasmaterias')),
            ],
        ),
    ]
