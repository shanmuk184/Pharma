from django.urls import path
from .views import hello, hyu

urlpatterns = [
    path('hello', hello),
    path('hyu', hyu)
    ]