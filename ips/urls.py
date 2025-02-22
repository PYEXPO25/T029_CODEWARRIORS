from slotfinder.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    path('reserve/<int:slot_id>/', views.reserve_parking, name='reserve_parking'),
    path('payment/<int:reservation_id>/', views.make_payment, name='make_payment'),
    path('available-slots/',views.available_slots, name='available_slots'),
    path('check-expired/', views.check_expired_reservations, name='check_expired_reservations'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('slotfinder.urls')),  # Include myapp URLs
]

