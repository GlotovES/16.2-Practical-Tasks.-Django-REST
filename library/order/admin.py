from django.contrib import admin
from .models import Order

@admin.action(description='Close selected orders')
def close_orders(modeladmin, request, queryset):
    queryset.update(status='closed')  # Adjust status field as needed

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status')  # Adjust fields as needed
    actions = [close_orders]

admin.site.register(Order,OrderAdmin)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'status', 'created_at')
    list_filter = ('status', 'created_at')