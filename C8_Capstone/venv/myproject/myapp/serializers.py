from rest_framework import serializers
from .models import Booking, Menu


class BookingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'name', 'No_of_guests',
                  'reservation_date', 'reservation_slot']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price']
