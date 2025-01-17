from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .models import ProductDB, CustomerDB, PlacedOrderDB, CartDB
from django.views import View

# Create your views here.

# ********* Home Page ********** #
class ProductView(View):
 def get(self, request):
  topwears = ProductDB.objects.filter(category = "TW")
  bottomwears = ProductDB.objects.filter(category = "BW")
  mobiles = ProductDB.objects.filter(category = "M")
  return render(request, 'product/home.html', {'topwears':topwears, 'bottomwears':bottomwears, 'mobiles':mobiles})

# ********* Product Detail page ********** #
class ProductDetailView(View):
 def get(self, request, id):
  product = ProductDB.objects.get(pk = id)
  return render(request, 'product/Productdetail.html', {'product' : product})
  
  
# ********* Add to Cart Page ********** #
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

# def mobile(request):
#  return render(request, 'product/mobile.html')
class MobileView(View):
 def get(self, request, slug = None):
  if slug == None: 
   mobile_page = ProductDB.objects.filter(category="M")
  elif slug == 'MicroMax' or slug == 'Apple':
   mobile_page = ProductDB.objects.filter(category="M").filter(brand = slug)
  elif slug == 'below':
   mobile_page = ProductDB.objects.filter(category="M").filter(discounted_price__lt = 30000)
  elif slug == 'above':
   mobile_page = ProductDB.objects.filter(category="M").filter(discounted_price__gt = 30000)
  return render(request, 'product/mobile.html', {'mobile_page' : mobile_page})

class ClothWearView(View):
 def get(self, request, slug = None):
  if slug == None:
   qs1 = ProductDB.objects.filter(category = "BW")
   qs2 = ProductDB.objects.filter(category = "TW")
   clothes_page = qs2.union(qs1)
  elif slug == "BW":
   clothes_page = ProductDB.objects.filter(category = "BW")
  elif slug == 'TW':
   clothes_page = ProductDB.objects.filter(category = "TW")
  elif slug == 'ShilpVastra' or slug == "Polo" or slug =="Velvet":
   clothes_page = ProductDB.objects.all().filter(brand = slug)
  return render(request, 'product/clothing.html', {"clothes_page" : clothes_page})

def login(request):
 return render(request, 'customer/login.html')

def customerregistration(request):
 return render(request, 'customer/customerregistration.html')

def checkout(request):
 return render(request, 'orders/checkout.html')
