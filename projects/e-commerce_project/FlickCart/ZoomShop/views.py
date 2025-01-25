from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect 
from .models import ProductDB, CustomerDB, PlacedOrderDB, CartDB
from django.views import View
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from django.contrib import messages
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
  
  
# ********* Cart Page ********** #
def add_to_cart(request):
 product_id = request.GET.get('product_id')
 print("Prodct ID:::", product_id)
 C_product = ProductDB.objects.get(id = product_id)
 print("Pruct::",C_product)
 CartDB(user=request.user, product=C_product).save()
 return redirect('/cart/')
 

def show_cart(request):
 if request.user.is_authenticated:
  products = CartDB.objects.filter(user = request.user)
  amount = 0.0
  shipping_charges = 70
  discount = 0.0
  total_amount = 0.0
  cart_product = [prod for prod in CartDB.objects.all() if prod.user == request.user]
  if cart_product:
   for p in cart_product:
    total_amount_temp = (p.quantity * p.product.discounted_price) 
    amount += total_amount_temp
    total_amount = amount + shipping_charges
   return render(request, 'orders/addtocart.html', {'products' : products, 'amount':amount, 'total_amount':total_amount, 'discount':discount})
  else:
   return render(request, 'orders/addtocart.html')
 


# ********* Buy  ********** #
def buy_now(request):
 return render(request, 'orders/buynow.html')

# ********* Profile view ********** #
class ProfileView(View):
 def get(self, request):
  form = UserProfileForm()
  return render(request, 'customer/profile.html', {'form':form, 'active':'btn-primary'})
 
 def post(self, request):
  form = UserProfileForm(request.POST)
  if form.is_valid():
   name = form.cleaned_data['name']
   locality = form.cleaned_data['locality']
   city = form.cleaned_data['city']
   zipcode = form.cleaned_data['zipcode']
   state = form.cleaned_data['state']
   user = CustomerDB(user= request.user, name=name, locality=locality, city=city, zipcode=zipcode, state=state)
   user.save()
   messages.success(request,'Profile has been Updated Successfully!!.')
  return render(request, 'customer/profile.html',{'form':form, 'active':'btn-primary'})

def CustomerAddress(request):
 address = CustomerDB.objects.filter(user=request.user)
 return render(request, 'customer/address.html', {'address':address, 'active':'btn-primary'})

def orders(request):
 return render(request, 'orders/orders.html')

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


class UserRegistrationFormView(View):
 def get(self, request):
  form = UserRegistrationForm()
  return render(request, 'customer/customerregistration.html', {'form':form})
 
 def post(self, request):
  form = UserRegistrationForm(request.POST)
  if form.is_valid():
   form.cleaned_data
   messages.success(request, 'Registration Successfull !.')
   form.save()
  return render(request, 'customer/customerregistration.html', {'form':form})

def checkout(request):
 return render(request, 'orders/checkout.html')
