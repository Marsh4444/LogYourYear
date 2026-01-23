from pprint import pprint
from django.contrib.auth.models import User
from core.models import Restaurant,Rating, Sale
from django.utils import timezone
from django.db import connection

def run():
    user = User.objects.first()
    restaurant = Restaurant.objects.first()

    print(Rating.objects.get_or_create(
        restaurant=restaurant,
        user=user,
        rating=4
    ))

    pprint(connection.queries)




    