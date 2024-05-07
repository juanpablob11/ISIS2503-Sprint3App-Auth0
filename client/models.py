from django.db import models

class Cliente(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('gerente', 'Gerente'),
        ('cliente', 'Cliente'),
    )
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    numero_celular = models.CharField(max_length=20)
    correo_electronico = models.EmailField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='cliente')

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.role}"
