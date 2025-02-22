"""
URL configuration for ips project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from slotfinder.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    path('reserve/<int:slot_id>/', views.reserve_parking, name='reserve_parking'),
    path('payment/<int:reservation_id>/', views.make_payment, name='make_payment'),
    path('available-slots/',views.available_slots, name='available_slots'),
    path('check-expired/', views.check_expired_reservations, name='check_expired_reservations'),
]
# myproject/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('slotfinder.urls')),  # Include myapp URLs
]

