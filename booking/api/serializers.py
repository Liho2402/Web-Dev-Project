from rest_framework import serializers
from .models import Tour, Hotel, Booking, Review

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class BookingSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    tour = serializers.PrimaryKeyRelatedField(queryset=Tour.objects.all())
    booking_date_from = serializers.DateField(read_only=True)
    booking_date_to = serializers.DateField(read_only=True)

class ReviewSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all())
    rating = serializers.IntegerField()
    comment = serializers.CharField()
    published_time = serializers.DateTimeField(read_only=True)