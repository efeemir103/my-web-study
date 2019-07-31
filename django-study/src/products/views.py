from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductModelForm, RawProductForm

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

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=my_id)
    # obj = get_object_or_404(Product, id=my_id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # POST request
    if request.method == "POST":
        # Confirming delete
        obj.delete()
        return redirect("../")
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)

def product_create_view(request):
    initial_data = {
        'title': "My awesome title"
    }
    form = ProductModelForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = ProductModelForm()
    
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)