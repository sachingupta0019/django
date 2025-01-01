from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
 return render(request, 'product/home.html')

def product_detail(request):
 return render(request, 'product/productdetail.html')

def add_to_cart(request):
 return render(request, 'orders/addtocart.html')

def buy_now(request):
 return render(request, 'orders/buynow.html')

def profile(request):
 return render(request, 'customer/profile.html')

def address(request):
 return render(request, 'customer/address.html')

def orders(request):
 return render(request, 'orders/orders.html')

def change_password(request):
 return render(request, 'customer/changepassword.html')

def mobile(request):
 return render(request, 'product/mobile.html')

def login(request):
 return render(request, 'customer/login.html')

def customerregistration(request):
 return render(request, 'customer/customerregistration.html')

def checkout(request):
 return render(request, 'orders/checkout.html')
