from django.shortcuts import render

# Create your views here.
from helpers.goibibo import get_ibibo_data
from information.models import information
from django.http import HttpResponse

def populate_goibibo(request):
    for i in get_ibibo_data():
        hotel=information(name=i['hn'],
                          location=i['l'],
                          hotel_code=i['hc'])
        hotel.save()
    return HttpResponse(html)

