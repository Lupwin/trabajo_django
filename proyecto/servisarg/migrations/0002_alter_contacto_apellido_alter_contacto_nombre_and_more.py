# Generated by Django 4.2 on 2023-05-23 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("servisarg", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contacto",
            name="apellido",
            field=models.CharField(max_length=100, verbose_name="Apellido"),
        ),
        migrations.AlterField(
            model_name="contacto",
            name="nombre",
            field=models.CharField(max_length=100, verbose_name="Nombre"),
        ),
        migrations.AlterField(
            model_name="trabajador",
            name="clave",
            field=models.CharField(max_length=20, verbose_name="Contraseña"),
        ),
    ]