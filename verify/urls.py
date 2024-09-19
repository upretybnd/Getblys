from django.urls import path
from .views import verification

urlpatterns = [
    path('api/verify/', verification, name='verification'),
]
