# Generated by Django 3.1.1 on 2020-10-02 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_curso_image_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_estreno', models.DateField()),
                ('mayores_de', models.IntegerField(default=0)),
                ('preventa_online', models.BooleanField(default=False)),
            ],
        ),
    ]
