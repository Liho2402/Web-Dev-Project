from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg
from .models import Review, Hotel

@receiver([post_save, post_delete], sender=Review)
def update_hotel_rating(sender, instance, **kwargs):
    hotel = instance.hotel
    avg_rating = hotel.review_set.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0.0
    hotel.rating = round(avg_rating, 2)
    hotel.save()
