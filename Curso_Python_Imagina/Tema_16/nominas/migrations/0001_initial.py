# Generated by Django 4.2.2 on 2023-06-18 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nomina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_empleado', models.IntegerField()),
                ('salario', models.IntegerField()),
            ],
        ),
    ]
