from django.shortcuts import render
from django.http import JsonResponse
from .models import Hotel
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Tour, Hotel, Booking
from .serializers import TourSerializer, HotelSerializer, BookingSerializer
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['GET'])
def get_tours(request):
    query = request.GET.get('search')
    tours = Tour.objects.filter(name__icontains=query) if query else Tour.objects.all()
    serializer = TourSerializer(tours, many=True)
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

# @api_view(['GET'])
# def get_hotels(request):
#     query = request.GET.get('search')
#     hotels = Hotel.objects.filter(namr__icontains=query) if query else Tour.objects.all()
#     serializer = HotelSerializer(hotels, many=True)
#     return Response(serializer.data)

class HotelList(APIView):
    def get(self, request):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

class TourDetail(APIView):
    def get(self, request, pk):
        tour = Tour.objects.get(pk=pk)
        serializer = TourSerializer(tour)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username and password:
        user = User.objects.create_user(username=username, password=password)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return Response({'error': 'Invalid data'}, status=400)


# def post_list(request):
#     hotels = Hotel.objects.order_by('rating')
#     return render(request, 'hotels/', {'hotels' : hotels})



# def hotels_list(request):
#     hotels = Hotel.objects.all()
#     hotels_json = [h.to_json() for h in hotels]

#     return JsonResponse(hotels, safe=False)