from django.contrib import admin
from . models import Customer, Rooms, Order, OrderItem, UpdateOrder,Contact, CheckoutDetail

# Register your models here.
admin.site.register(Customer)
admin.site.register(Rooms)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(CheckoutDetail)
admin.site.register(UpdateOrder)