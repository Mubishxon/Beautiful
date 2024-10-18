from django.shortcuts import render
from .models import kasmetika
# Create your views here.
def asosiypage(request):

    habar = "salom hammaga"
    return render(request, 'index.html', context={"habar": habar})


def about(request):
    return render(request, 'about.html', context={})
def client(request):
    return render(request, 'client.html', context={})
def contact(request):
    return render(request, 'contact.html', context={})
def products(request):

    kasmetika = 'kasmetika'.objects.all()
    context = {
            "kasmetika": kasmetika
    }
    return render(request, 'products.html', context=context)