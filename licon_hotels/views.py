from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . inherit import cartData

# Create your views here.
def index(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']

    products = Rooms.objects.all()
    return render(request, "index.html", {'products':products, 'cartItems':cartItems})
