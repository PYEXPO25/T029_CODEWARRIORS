from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from slotfinder.models import ParkingSlot, Reservation, Payment
from datetime import timedelta

# API to update parking slot availability from IoT device
def update_parking_slot_status(request, slot_id):
    slot = ParkingSlot.objects.get(id=slot_id)
    status = request.POST.get('status')  # 'occupied' or 'vacant'

    if status == 'occupied':
        slot.is_available = False
    else:
        slot.is_available = True

    slot.save()

    return JsonResponse({'message': f"Slot {slot.slot_number} updated to {status}"})
# Reserve a parking slot
def reserve_parking(request, slot_id):
    parking_slot = get_object_or_404(ParkingSlot, id=slot_id)

    if not parking_slot.is_available:
        return JsonResponse({'error': 'Parking slot is not available'}, status=400)

    time_limit = int(request.POST.get('time_limit', 1))

    reserved_from = timezone.now()
    reservation = Reservation.objects.create(
        user="User1",  # Replace with actual user info
        parking_slot=parking_slot,
        reserved_from=reserved_from,
        time_limit=time_limit
    )

    parking_slot.is_available = False  # Slot is now reserved
    parking_slot.save()

    return JsonResponse({
        'message': 'Reservation successful',
        'reservation_id': reservation.id,
        'reserved_until': reservation.reserved_until,
    })

# Process payment for reservation
def make_payment(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    # Calculate the amount based on time limit
    amount = reservation.parking_slot.price_per_hour * reservation.time_limit

    # Simulate payment (replace with actual payment gateway like Stripe)
    payment = Payment.objects.create(
        reservation=reservation,
        amount=amount,
        payment_status='Pending',
    )

    payment.payment_status = 'Completed'  # Mark payment as completed
    payment.save()

    return JsonResponse({
        'message': 'Payment successful',
        'payment_status': payment.payment_status,
        'amount': amount,
    })

# Check expired reservations and release parking slots
def check_expired_reservations():
    expired_reservations = Reservation.objects.filter(reserved_until__lt=timezone.now())

    for reservation in expired_reservations:
        parking_slot = reservation.parking_slot
        parking_slot.is_available = True  # Release the slot
        parking_slot.save()

        reservation.delete()  # Cancel the reservation

    return JsonResponse({'message': 'Expired reservations have been cancelled'})
def available_slots(request):
    # Get all parking slots that are available
    available_slots = ParkingSlot.objects.filter(is_available=True)

    # Prepare the list of available slots with their details
    slots_data = []
    for slot in available_slots:
        slots_data.append({
            'slot_number': slot.slot_number,
            'location': slot.location,
            'price_per_hour': str(slot.price_per_hour),
        })
    
    return JsonResponse({'available_slots': slots_data})

def index(request):
    return render(request, 'myapp/index.html')
