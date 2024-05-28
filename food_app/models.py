# models.py
from django.db import models
from django.utils import timezone


    
class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=50)
    duration_days = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    lunch_price = models.DecimalField(max_digits=5, decimal_places=2)
    dinner_price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    CATEGORY_CHOICES = [
        ('Basic', 'Basic'),
        ('Premium', 'Premium'),
    ]
    category = models.CharField(max_length=7, choices=CATEGORY_CHOICES)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    lunch_off = models.BooleanField(default=False)
    dinner_off = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    def can_order_lunch(self):
        if self.lunch_off:
            return False
        current_time = timezone.now().time()
        if (current_time >= timezone.make_aware(timezone.datetime.strptime("00:00", "%H:%M")).time() and
            current_time < timezone.make_aware(timezone.datetime.strptime("09:00", "%H:%M")).time()):
            return False
        return True
    
    def can_order_dinner(self):
        if self.dinner_off:
            return False
        current_time = timezone.now().time()
        if (current_time >= timezone.make_aware(timezone.datetime.strptime("12:00", "%H:%M")).time() and
            current_time < timezone.make_aware(timezone.datetime.strptime("15:00", "%H:%M")).time()):
            return False
        return True
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.customer.can_order_lunch():
            self.lunch = False
        if not self.customer.can_order_dinner():
            self.dinner = False
        super(Order, self).save(*args, **kwargs)
