from django.urls import path
from . import views
from django.urls import path
from .views import get_tours, create_booking, HotelList, TourDetail, register_user
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('tours/', get_tours),
    path('bookings/', create_booking),
    path('hotels/', HotelList.as_view()),
    path('tours/<int:pk>/', TourDetail.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('register/', register_user),
    path('token/refresh/', TokenRefreshView.as_view()),
    # path('', views.post_list, name='post_list')
]
