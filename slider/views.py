from django.shortcuts import render
from .models import SliderImage


def home(request):
    slider_images = SliderImage.objects.all()
    return render(request, 'slider/home.html', {'slider_images': slider_images})
