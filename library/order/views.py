from django.contrib.auth.decorators import login_required
from .models import Order
from django.shortcuts import render, redirect
from .forms import OrderForm
from rest_framework import viewsets
from .models import User, Order, Book, Author
from .serializers import OrderSerializer

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'my_orders.html', {'orders': orders})

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('my_orders')  
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer