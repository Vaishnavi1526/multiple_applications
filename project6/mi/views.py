from django.shortcuts import render
from django.http import HttpResponse
def boomra(request):
    return HttpResponse("<h1><center>Boomra page</center></h1>")
def klrahul(request):
    return render(request,'klrahul.html')


