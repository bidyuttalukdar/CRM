from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    # return HttpResponse('Home page')
    return render(request,'accounts/dashboard.html')
def about(request):
    return HttpResponse('About page')
def products(request):
    return render(request,'accounts/product.html')
def customer(request):
    return render(request,'accounts/customer.html')
