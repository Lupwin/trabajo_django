# Generated by Django 4.2 on 2023-06-09 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("servisarg", "0003_remove_mensaje_contenido_remove_mensaje_emisor_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trabajador",
            name="usuario",
            field=models.CharField(max_length=100, unique=True, verbose_name="Usuario"),
        ),
    ]