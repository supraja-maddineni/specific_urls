from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return HttpResponse('<h1>MSD is the Best Finisher in the world</h1>')