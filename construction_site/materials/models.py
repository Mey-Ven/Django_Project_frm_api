from django.db import models
from django.contrib.auth.models import User

class Material(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # L'utilisateur qui commande
    material = models.ForeignKey(Material, on_delete=models.CASCADE)  # Matériau commandé
    quantity = models.PositiveIntegerField()  # Quantité commandée
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.material.name} ({self.quantity})"