from django.shortcuts import render
from .models import Pizza

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by()
    context = {'pizzas': pizzas}

    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id = pizza_id)
    ingredi = pizza.topping_set.all()
    context = {'pizza': pizza, 'ingredientes':ingredi}

    return render(request, 'pizzas/ingredientes.html', context)