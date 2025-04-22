from django.contrib import admin
from .models import Hotel, Booking, Tour, Review
# Register your models here.

admin.site.register(Hotel)
admin.site.register(Booking)
admin.site.register(Tour)
admin.site.register(Review)