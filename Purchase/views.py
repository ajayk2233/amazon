from django.shortcuts import render,HttpResponse

def show(request):
    return HttpResponse('Purchase show page')