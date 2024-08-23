from django.urls import path
from .views import AboutUs, Success

urlpatterns = [
    path('about/', AboutUs.as_view()),
    path('success/', Success.as_view()),
]
