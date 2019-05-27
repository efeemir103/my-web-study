from django.shortcuts import render

from .forms import ProductForm

from .models import Product
# Create your views here.
def product_create_view(request,*args, **kwargs): # *args, **kwargs
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form':form
    }
    return render(request,"product_create.html",context)

def product_detail_view(request,*args, **kwargs): # *args, **kwargs
    obj = Product.objects.get(id=1)
    context = {
    "object":obj
    }
    return render(request,"product_detail.html",context)