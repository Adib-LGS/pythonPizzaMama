from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Pizza

# Create your views here.


def index(request):
    """pizzas = Pizza.objects.all()
    pizzas_names_and_price = [pizza.name + ' - ' + str(pizza.price) + ' $' for pizza in pizzas]
    pizzas_names_and_price_str = ', '.join(pizzas_names_and_price)
    return HttpResponse('Pizzas : ' + pizzas_names_and_price_str)"""
    pizza = Pizza.objects.all().order_by('price')
    return render(request, 'menu/index.html', {'pizzas': pizza})


def api_get_pizza(request):
    pizza = Pizza.objects.all().order_by('price')
    json = serializers.serialize('json', pizza)
    return HttpResponse(json)