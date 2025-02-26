from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = [
        ('ADMIN', 'Administrador'),
        ('SUPERVISOR', 'Supervisor'),
        ('USUARIO', 'Usuario'),
    ]
    rol = models.CharField(max_length=15, choices=ROLES, default='USUARIO')

    def es_admin(self):
        return self.rol == 'ADMIN'

    def es_supervisor(self):
        return self.rol == 'SUPERVISOR'

    def es_usuario(self):
        return self.rol == 'USUARIO'