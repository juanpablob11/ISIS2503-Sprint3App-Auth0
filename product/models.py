from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    nombre = models.CharField(max_length=255)
    score_de_confiabilidad = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)]
    )
    cliente = models.ForeignKey(
        'Cliente',  # Usando el nombre de la clase como string para evitar problemas de importación
        on_delete=models.CASCADE,  # Asegura que si se elimina un Cliente, sus Productos asociados también se eliminen
        related_name='productos'  # Facilita el acceso inverso desde Cliente a Productos
    )

    def __str__(self):
        return f"{self.nombre} - Score: {self.score_de_confiabilidad}, Cliente: {self.cliente.nombres}"
