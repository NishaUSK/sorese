from django.shortcuts import render
from django.utils import timezone
from .models import Process


def base(request):
    return render(request, 'home/base.html', {})

def footer(request):
    return render(request, 'home/footer.html', {})

def header(request):
    return render(request, 'home/header.html', {})

def jumbotron1(request):
    return render(request, 'home/jumbotron1.html', {})

def jumbotron2(request):
    return render(request, 'home/jumbotron2.html', {})

def jumbotron3(request):
    gyanpages = Gyanpage.objects.filter(gyantitle='title')
    return render(request, 'home/jumbotron3.html', {'gyanpages': gyanpages})
