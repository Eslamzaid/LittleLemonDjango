from rest_framework import serializers
from .models import MenuItem, Booking

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"