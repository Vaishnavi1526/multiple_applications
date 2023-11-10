from django.shortcuts import render
from django.http import HttpResponse

def msd(request):
    return HttpResponse("<h1><marquee>MS DHONI IS THE BEST CAPTAIN</marquee></h1>")
def raina(request):
    return render(request,'raina.html')
  
