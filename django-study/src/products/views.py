from django.shortcuts import render

from .models import Product
# Create your views here.
def product_detail_view(request,*args, **kwargs): # *args, **kwargs
    obj = Product.objects.get(id=1)
    context = {
    "object":obj
    }
    return render(request,"index.html",context)
