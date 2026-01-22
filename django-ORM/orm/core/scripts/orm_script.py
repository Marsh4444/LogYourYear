from django.contrib.auth.models import User
from core.models import Restaurant,Rating
from django.utils import timezone
from django.db import connection

def run():
    print(Rating.objects.filter(rating__lte=3))
    #print(Rating.objects.filter(rating=4))

    print(connection.queries)
    