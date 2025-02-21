from ips.urls import path
from . import views
from ips import views as iot_views

urlpatterns = [
    path('reserve/<int:slot_id>/', views.reserve_parking, name='reserve_parking'),
    path('payment/<int:reservation_id>/', views.make_payment, name='make_payment'),
    path('check-expired/', views.check_expired_reservations, name='check_expired_reservations'),
    path('update-slot/<int:slot_id>/', iot_views.update_parking_slot_status, name='update_parking_slot_status'),
]
