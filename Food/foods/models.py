from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
        ('completed', 'Completed'),
    ]
    
    customer_name = models.CharField(max_length=100)
    food_name = models.CharField(max_length=100)
    restaurant = models.CharField(max_length=100, default='Unknown Restaurant')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.10)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name} - {self.food_name}"
    
    def get_total_price(self):
        """Calculate total price (price * quantity)"""
        if self.quantity is None or self.price is None:
            return 0
        return self.price * self.quantity  # ✅ Fixed