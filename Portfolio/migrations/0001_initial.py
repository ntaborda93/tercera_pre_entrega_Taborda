# Generated by Django 4.1.4 on 2023-01-08 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="adopcion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=256)),
                ("apellido", models.CharField(max_length=256)),
                ("email", models.EmailField(max_length=254)),
                ("provincia", models.CharField(max_length=256)),
                ("localidad", models.CharField(max_length=256)),
                ("tipo_vivienda", models.CharField(max_length=256)),
                ("cantidad_mascotas", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="entrega",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=256)),
                ("fecha_entrega", models.DateTimeField()),
                ("esta_aprobado", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Gato",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=64)),
                ("color_de_ojos", models.CharField(max_length=64)),
                ("fecha_aprox_nacimiento", models.DateField(null=True)),
                ("color_pelaje", models.CharField(max_length=64)),
                ("genero", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="transito",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=256)),
                ("apellido", models.CharField(max_length=256)),
                ("email", models.EmailField(max_length=254)),
                ("provincia", models.CharField(max_length=256)),
                ("localidad", models.CharField(max_length=256)),
                ("codigo_postal", models.IntegerField()),
                ("posecion", models.BooleanField()),
                ("bio", models.TextField(null=True)),
            ],
        ),
    ]
