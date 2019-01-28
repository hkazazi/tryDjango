from django.shortcuts import render
from .models import Product
from .forms import ProductForm #RawProductForm
# Create your views here.

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#
#     context = {
#          'form' : my_form
#     }
#     return render(request, 'products/product_create.html',context)


# def product_create_view(request):
    # print(request.GET)
    # print(request.POST)
    # title = request.POST.get('title')
    # print(title)
    # context = {}
    # return render(request, 'products/product_create.html',context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    form = ProductForm()

    context = {'form':form}
    return render(request, 'products/product_create.html',context)


def product_detail_veiw(request):


    obj = Product.objects.get(id=3)
    # context = {
    #     'title':obj.title,
    #     'description': obj.description,
    # }
    context = {'object':obj}
    return render(request, 'products/product_detail.html',context)