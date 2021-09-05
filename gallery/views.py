from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt

# Create your views here.


def index(request):
    date = dt.date.today()
    # images = Image.get_images()
    # location = Location.get_location()
    # locations = Location.get_location()

    return render(request, 'index.html', {"date": date})