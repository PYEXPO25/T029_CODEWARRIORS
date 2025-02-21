from django.contrib import admin
from .models import ParkingSlot, Reservation, Payment

admin.site.register(ParkingSlot)
admin.site.register(Reservation)
admin.site.register(Payment)
