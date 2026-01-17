from django.shortcuts import redirect, render , get_object_or_404   
from django.db.models import Sum, Count
from decimal import Decimal

from .models import Order

# Create your views here.

#home view
def home(request):
    #gets all active orders from the database
    active_orders = Order.objects.exclude(status='completed').order_by('-created_at')

    #gets all completed orders from the database
    completed_orders_list = Order.objects.filter(status='completed').order_by('-updated_at')
    
    # Calculate stats for the dashboard
    pending_orders = Order.objects.filter(status='pending').count()
    preparing_orders = Order.objects.filter(status='preparing').count()
    ready_orders = Order.objects.filter(status='ready').count()
    completed_orders_count = Order.objects.filter(status='completed').count()
    total_spent = Order.objects.filter(status='completed').aggregate(Sum('price'))['price__sum'] or 0
    total_spent = round(total_spent, 2)
    restaurants_count = Order.objects.values('restaurant').distinct().count()

    context = {
        'active_orders': active_orders,
        'completed_orders_list': completed_orders_list,
        'pending_orders': pending_orders,
        'preparing_orders': preparing_orders,
        'ready_orders': ready_orders,
        'completed_orders_count': completed_orders_count,
        'total_spent': total_spent,
        'restaurants_count': restaurants_count,
    }
    return render(request, 'foods/home.html', context)


# Create order view
def create_order(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        food_name = request.POST['food_name']
        restaurant = request.POST.get('restaurant', 'Unknown Restaurant')
        quantity = int(request.POST.get('quantity', 1))
        price = Decimal(request.POST.get('price', '0.10'))

        # Create and save the new order
        new_order = Order(
            customer_name=customer_name,
            food_name=food_name,
            restaurant=restaurant,
            quantity=quantity,
            price=price,
            status='pending'
        )
        new_order.save()
        return redirect('order_confirm', pk=new_order.pk)
    


def order_confirm(request, pk):
    # Get the order or return 404 if not found
    order = get_object_or_404(Order, pk=pk)
    
    # Prepare context data
    context = {
        'order': order,
        'meal_name': order.food_name,
        'restaurant': order.restaurant,
        'price': order.price,
        'order_date': order.created_at,  # Assuming you have this field
        'order_id': order.pk,
    }
    
    return render(request, 'foods/order_comfirm.html', context)

def complete_order(request, pk):
    # Get the order or return 404 if not found
    order = get_object_or_404(Order, pk=pk)
    
    # Update the order status to 'completed'
    order.status = 'completed'
    order.save()
    
    return redirect('home')

def edit_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    
    if request.method == 'POST':
        order.customer_name = request.POST.get('customer_name')
        order.food_name = request.POST.get('food_name')
        order.restaurant = request.POST.get('restaurant')  # Use .get() instead of ['restaurant']
        order.quantity = int(request.POST.get('quantity', 1))
        order.price = request.POST.get('price')
        
        order.save()
        return redirect('home')
    
    return render(request, 'foods/edit_order.html', {'order': order})
    