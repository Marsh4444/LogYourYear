from django.db import models

# Create your models here.
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    food_name = models.CharField(max_length=100)  # was item_name
    order_status = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)  # was order_date

    def __str__(self):
        return f"Order {self.id} by {self.customer_name} for {self.quantity} x {self.food_name}"