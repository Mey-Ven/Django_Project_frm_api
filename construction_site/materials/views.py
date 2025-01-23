from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from .models import Material, Order
from .forms import OrderForm

def material_list(request):
    materials = Material.objects.all()
    return render(request, 'materials/material_list.html', {'materials': materials})

def order_list(request):from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from .models import Material, Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def material_list(request):
    materials = Material.objects.all()
    return render(request, 'materials/material_list.html', {'materials': materials})

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'materials/order_list.html', {'orders': orders})

@login_required
def order_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))
        if quantity > 0 and material.quantity >= quantity:
            material.quantity -= quantity
            material.save()
            order = Order.objects.create(user=request.user, material=material, quantity=quantity)
            messages.success(request, 'Order placed successfully!')
            return redirect('order_list')
        else:
            messages.error(request, 'Invalid quantity or insufficient stock.')
    return render(request, 'materials/order_material.html', {'material': material})
    orders = Order.objects.filter(user=request.user)
    return render(request, 'materials/order_list.html', {'orders': orders})

def order_material(request, material_id):
    if request.method == 'POST':
        material = get_object_or_404(Material, id=material_id)
        quantity = int(request.POST.get('quantity', 0))
        if quantity > 0 and material.quantity >= quantity:
            material.quantity -= quantity
            material.save()
            order = Order.objects.create(user=request.user, material=material, quantity=quantity)
            return redirect('order_list')
    return render(request, 'materials/order_material.html', {'material_id': material_id})