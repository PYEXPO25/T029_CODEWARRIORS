from django.db import models
from django.utils import timezone
from datetime import timedelta

class ParkingSlot(models.Model):
    slot_number = models.CharField(max_length=10, unique=True)
    is_available = models.BooleanField(default=True)  # Slot availability status
    location = models.CharField(max_length=255)  # Location (e.g., floor, section)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)  # Price per hour for parking slot

    def __str__(self):
        return f"Slot {self.slot_number} at {self.location}"

class Reservation(models.Model):
    TIME_LIMIT_CHOICES = [
        (1, '30 minutes'),
        (2, '90 minutes'),
        (3, '120 minutes'),
    ]
    
    user = models.CharField(max_length=255)  # Replace with actual user info
    parking_slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    reserved_from = models.DateTimeField()
    reserved_until = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    time_limit = models.IntegerField(choices=TIME_LIMIT_CHOICES, default=1)  # 1 hour, 2 hours, or 3 hours

    def save(self, *args, **kwargs):
        if not self.reserved_until:
            self.reserved_until = self.reserved_from + timedelta(hours=self.time_limit)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reservation for {self.parking_slot.slot_number} by {self.user}"

class Payment(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for reservation {self.reservation.id} - {self.payment_status}"
