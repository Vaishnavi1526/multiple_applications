from django.shortcuts import render
from django.http import HttpResponse
def virat(request):
    return HttpResponse("<h1>Virat</h1>")
def sachin(request):
    return render(request,'sachin.html')
