# Generated by Django 3.1.2 on 2020-10-24 00:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_contacto_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.curso')),
            ],
        ),
    ]
