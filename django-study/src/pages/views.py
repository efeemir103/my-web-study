from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs): # *args, **kwargs
    return render(request,"index.html",{})