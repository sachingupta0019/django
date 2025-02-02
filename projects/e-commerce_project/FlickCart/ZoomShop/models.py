from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.

# ****************** Customer Model ******************* #
STATE_CHOICES = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal"),
)

class CustomerDB(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    locality = models.CharField(max_length=256)
    city = models.CharField(max_length=128)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)
    
# ****************** Product Model ******************* #
CATEGORY_CHOICES = (
    ("M" , "Mobile"),
    ("L" , "Laptop"),
    ("TW", "Top Wear"),
    ("BW", "Bottom Wear"),
)
class ProductDB(models.Model):
    title = models.CharField(max_length=128)
    tag = models.CharField(max_length=128)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=128)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    product_image = models.ImageField(upload_to='media/productImage')

    def __str__(self):
        return str(self.id)
    

# ****************** Cart Model ******************* #

class CartDB(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductDB, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
# ****************** Order Placed Model ******************* #
ORDER_PLACED_CHOICES = (
    ("Pending" , "Pending"),
    ("Delivered", "Delivered"),
    ("Cancel", "Cancel"),
)

class PlacedOrderDB(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerDB, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductDB, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_placed_date  = models.DateField(auto_now_add=True)
    order_delivered_date = models.DateField(auto_now_add=True)
    order_cancel_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=ORDER_PLACED_CHOICES, max_length=50, default='Pending')
    
    def __str__(self):
        return str(self.id)
        