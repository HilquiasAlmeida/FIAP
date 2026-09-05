from django.shortcuts import render
from .models import ChildDevice

def index(request):
    devices = ChildDevice.objects.all()
    return render(request, 'tracker/index.html', {'devices': devices})
