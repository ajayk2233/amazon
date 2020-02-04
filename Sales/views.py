from django.shortcuts import render,HttpResponse
from .models import Order,OrderForm,User,Product
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

def ShowView(request):
    if request.method == 'POST':
        filter_b = request.POST.get('filter_by')
        print(filter_b)
    else:
        filter_b = None
    object_list = Product.objects.all()
    return render(request,'Sales/product_list.html',{'object_list':object_list,'filter_by':filter_b})

class AddView(CreateView):
    model = Product
    fields = '__all__'
    success_url = '/Sales/ShowView'

def DetailsView(request,id):
    details = Product.objects.get(id=id)
    return render(request, 'Sales/Product_Details.html',{'details':details})

class EditView(UpdateView):
    model = Product
    fields = '__all__'
    success_url = '/Sales/ShowView'
    def get_queryset(self):
        id = self.kwargs['pk']
        return Product.objects.filter(pk=id)