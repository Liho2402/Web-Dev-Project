from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    location = models.CharField(max_length=200)
    image_url = models.URLField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    book = models.BooleanField(default=False)

    def book(self):
        self.book = True
        self.save()

    def __str__(self):
        return f"{self.name} --- {self.rating}"
    
class Tour(models.Model):
    name = models.CharField(max_length=100)
    people = models.IntegerField()
    country_from = models.CharField(max_length=100)
    country_to = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desciprition = models.TextField()
    book = models.BooleanField(default=False)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)

    def book(self):
        self.book = True
        self.save()

    def __str__(self):
        return f"{self.name} --- {self.people} people"
        
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    comment = models.TextField()
    published_time = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    booking_date_from = models.DateField(blank=True, null=True)
    booking_date_to = models.DateField(blank=True, null=True)

