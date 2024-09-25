from django.shortcuts import render
from .models import Menu
from django.http import HttpResponse

# Create your views here.
def menu(request):
    menu_items = Menu.objects.all()