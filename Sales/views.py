from django.shortcuts import render,HttpResponse,redirect
from .models import Order,OrderForm,User,Product
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth import logout

def ShowView(request):
    object_list = Product.objects.all()
    if request.method == 'POST':
        filter_b = request.POST.get('filter_by')
        print(filter_b)
        if filter_b == None:
            object_list = object_list
        elif filter_b == 'low':
            object_list = Product.objects.filter(product_price_filter='low')
        elif filter_b == 'medium':
            object_list = Product.objects.filter(product_price_filter='medium')
        else:
            object_list = Product.objects.filter(product_price_filter='high')
    else:
        pass
    return render(request,'Sales/product_list.html',{'object_list':object_list})
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

def DeleteView(request,id):
    data = Product.objects.get(id=id)
    data.delete()
    return redirect('/Sales/ShowView/')

def signin(request):
    return redirect('/admin/')

def signout(request):
    logout(request)
    return redirect('/Sales/ShowView/')