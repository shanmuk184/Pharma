from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from django.core import serializers
from django.forms.models import model_to_dict


# Create your views here.
def hello(request):
    data = list(Product.objects.values())
    return JsonResponse(data, safe=False)

def hyu(request):
    data = Product.objects.get(id=1)
    return JsonResponse(model_to_dict(data), safe=False)