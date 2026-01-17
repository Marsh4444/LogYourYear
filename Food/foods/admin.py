from django.contrib import admin
from foods.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'food_name', 'restaurant', 'quantity', 'price', 'status', 'get_total_price_display', 'created_at')
    list_filter = ('status', 'restaurant', 'created_at')
    search_fields = ('customer_name', 'food_name', 'restaurant')
    readonly_fields = ('created_at', 'updated_at', 'get_total_price_display')
    ordering = ('-created_at',)
    list_editable = ('status',)
    
    def get_total_price_display(self, obj):
        """Display total price in admin"""
        total = obj.get_total_price()
        if total == 0:
            return "Not calculated"
        return f"${total:.2f}"
    get_total_price_display.short_description = 'Total Price'

admin.site.register(Order, OrderAdmin)