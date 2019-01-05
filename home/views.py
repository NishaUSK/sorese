from django.shortcuts import render
from django.utils import timezone
from .models import Process
from .models import Heropage
from .models import Gyanpage
from .models import Footerpage

def base(request):
    return render(request, 'home/base.html', {})

def footer(request):
    return render(request, 'home/footer.html', {})

def header(request):
    return render(request, 'home/header.html', {})

def jumbotron1(request):
    heropages = Heropage.objects.get(herotitle="sample title")
    return render(request, 'home/jumbotron1.html', {'heropages': heropages})

def jumbotron2(request):
    return render(request, 'home/jumbotron2.html', {})

def jumbotron3(request):
    gyanpages = Gyanpage.objects.get(gyantitle='Share the knowledge')
    return render(request, 'home/jumbotron3.html', {'gyanpages': gyanpages})
