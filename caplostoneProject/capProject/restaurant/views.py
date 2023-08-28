from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import viewsets

# Create your views here.


def index(request):
    return render(request, 'index.html')


class MenuItemsView(generics.ListCreateAPIView):
    queryset =  MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()    
    serializer_class = BookingSerializer
    
    
    
    
    
    
    
    
    
    
    
# class bookingView(APIView):
#     def get(self, request):
#         item = Booking.objects.all()
#         serializer = bookingSerializer(item, many=True)
#         return Response(serializer.data)
    

# class menuView(APIView):
#     def post(self, request):
#         serializer = menuSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data})