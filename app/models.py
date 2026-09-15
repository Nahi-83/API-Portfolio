from django.db import models


class Projects(models.Model):

    id = models.IntegerField(primary_key=True)

    tituloproyecto = models.TextField(
        db_column='tituloProyecto',
        blank=True,
        null=False
    )

    descripcion = models.TextField(
        blank=True,
        null=False
    )

    rol = models.TextField(
        blank=True,
        null=False
    )

    tecnologias = models.TextField(
        blank=True,
        null=False
    )

    link = models.TextField(
        blank=True,
        null=False
    )

    class Meta:
        managed = True
        db_table = 'projects'