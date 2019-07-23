from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .forms import ProductForm, RawProductForm

from .models import Product
# Create your views here.

# def product_create_view(request,*args, **kwargs): # *args, **kwargs
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             print(my_form.cleaned_data) # Data as dict
#             Product.objects.create(**my_form.cleaned_data) # Slicing dict aas arguments and creating from data
#         else:
#             print(my_form.errors)
#     context = {
#         'form':my_form
#     }
#     return render(request127,"product_create.html",context)

def dynamic_lookup_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    # obj = get_object_or_404(Product, id=my_id)
    try:
        obj = Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

def product_create_view(request):
    initial_data = {
        'title': "My awesome title"
    }
    form = ProductForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = ProductForm()
    
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request,*args, **kwargs): # *args, **kwargs
    obj = Product.objects.get(id=1)
    context = {
    "object":obj
    }
    return render(request,"products/product_detail.html",context)