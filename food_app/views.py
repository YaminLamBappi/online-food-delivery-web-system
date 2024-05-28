# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from .models import Customer, Order, SubscriptionPlan
from django.utils import timezone
from django.http import HttpResponse

from datetime import datetime, time
from django.utils import timezone

def pay_subscription(request, customer_id, plan_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    plan = get_object_or_404(SubscriptionPlan, pk=plan_id)
    
    customer.balance += plan.price
    customer.plan = plan
    customer.save()
    
    return HttpResponse("Payment successful. Your subscription has been updated.")



def place_order(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    order = Order(customer=customer)
    
    if customer.balance < customer.plan.lunch_price + customer.plan.dinner_price:
        return render(request, 'customer_detail.html', {'customer': customer, 'error_message': "You have insufficient balance to place the order."})

    if not customer.lunch_off:
        order.lunch = True
        customer.balance -= customer.plan.lunch_price
    if not customer.dinner_off:
        order.dinner = True
        customer.balance -= customer.plan.dinner_price
            
    customer.save()
    order.save()
    return redirect('order_success', customer_id=customer.id)

def order_success(request, customer_id):
    return render(request, 'order_success.html', {'customer_id': customer_id})

def add_subscription(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    subscription_plans = SubscriptionPlan.objects.all()
    return render(request, 'add_subscription.html', {'customer': customer, 'subscription_plans': subscription_plans})


def admin_dashboard(request):
    today = now().date()
    orders = Order.objects.filter(date=today)
    
    lunch_basic = orders.filter(lunch=True, customer__category='Basic').count()
    lunch_premium = orders.filter(lunch=True, customer__category='Premium').count()
    dinner_basic = orders.filter(dinner=True, customer__category='Basic').count()
    dinner_premium = orders.filter(dinner=True, customer__category='Premium').count()

    context = {
        'lunch_basic': lunch_basic,
        'lunch_premium': lunch_premium,
        'dinner_basic': dinner_basic,
        'dinner_premium': dinner_premium,
    }

    return render(request, 'admin_dashboard.html', context)

def home(request):
    customers = Customer.objects.all()
    return render(request, 'home.html', {'customers': customers})



def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    error_message = None

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "lunch":
            customer.lunch_off = not customer.lunch_off
            customer.save()
        elif action == "dinner":
            customer.dinner_off = not customer.dinner_off
            customer.save()

    # Get current time
    current_time = timezone.localtime(timezone.now()).time()

    # Define time ranges
    lunch_start = time(0, 0)
    lunch_end = time(9, 0)
    dinner_start = time(0, 0)
    dinner_end = time(15, 0)
    both_start = time(0, 0)
    both_end = time(9, 0)

    # Determine if it's within the restricted time range for both
    within_both_restriction = both_start <= current_time <= both_end

    # Determine if it's within the restricted time range for lunch or dinner
    within_lunch_restriction = lunch_start <= current_time <= lunch_end
    within_dinner_restriction = dinner_start <= current_time <= dinner_end

    # Determine if customer should see lunch and/or dinner option
    show_lunch = not within_both_restriction and not within_lunch_restriction
    show_dinner = not within_both_restriction and not within_dinner_restriction
    show_both = not within_both_restriction
    # Get the last status
    lunch_status = "off" if customer.lunch_off else "on"
    dinner_status = "off" if customer.dinner_off else "on"

    return render(request, "customer_detail.html", {
        "customer": customer,
        "error_message": error_message,
        "show_lunch": show_lunch,
        "show_dinner": show_dinner,
        "current_time": current_time,
        "lunch_status": lunch_status,
        "dinner_status": dinner_status,
        "within_both_restriction": within_both_restriction,
    })
