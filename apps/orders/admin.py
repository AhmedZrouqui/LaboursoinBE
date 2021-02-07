from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'orderType', 'created_at')


admin.site.register(Order, OrderAdmin)