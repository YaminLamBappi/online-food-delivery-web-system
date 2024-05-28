from django.contrib import admin
from .models import SubscriptionPlan,Customer,Order
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'balance']
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ['name']
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer']

admin.site.register(SubscriptionPlan,SubscriptionPlanAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order,OrderAdmin)
