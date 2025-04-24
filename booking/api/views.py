from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Tour, Hotel, Booking
from .serializers import TourSerializer, HotelSerializer, BookingSerializer
from rest_framework import status


# Получаем список туров
@api_view(['GET'])
def get_tours(request):
    query = request.GET.get('search')
    tours = Tour.objects.filter(name__icontains=query) if query else Tour.objects.all()
    serializer = TourSerializer(tours, many=True)
    return Response(serializer.data)

# Список отелей 
@api_view(['GET'])
def get_hotels(request):
    query = request.GET.get('search')
    hotels = Hotel.objects.filter(name__icontains=query) if query else Hotel.objects.all()
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_booking(request):
    data = request.data.copy()
    data['user'] = request.user.id
    serializer = BookingSerializer(data=data)
    if serializer.is_valid():
        Booking.objects.create(user=request.user, tour_id=data['tour'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  Список отелей по id
class HotelList(APIView):
    def get(self, request, pk):
        hotels = Hotel.objects.get(pk=pk)
        serializer = HotelSerializer(hotels)
        return Response(serializer.data)
  
# Список туров по id
class TourDetail(APIView):
    def get(self, request, pk):
        tour = Tour.objects.get(pk=pk)
        serializer = TourSerializer(tour)
        return Response(serializer.data)