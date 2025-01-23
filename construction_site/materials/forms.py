from django import forms
from .models import Material

class OrderForm(forms.Form):
    material = forms.ModelChoiceField(queryset=Material.objects.all(), label="Matériau")  # Sélection du matériau
    quantity = forms.IntegerField(min_value=1, label="Quantité")  # Quantité à commander