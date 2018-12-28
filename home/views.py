from django.shortcuts import render


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
    return render(request, 'home/jumbotron3.html', {})
