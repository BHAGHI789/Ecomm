from django.db import models
from django.contrib.auth.models import User
# Create your models here.

Category_Choice=(
    ("ML","ML"),
    ("CR","CR"),
    ("LS","LS"),
    ("MS","MS"),
    ("PN","PN"),
    ("GH","GH"),
    ("CZ","CZ"),
    ("IC","IC")
)
class Product(models.Model):
    name=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    discription=models.TextField()
    compsition=models.TextField()
    category=models.CharField(choices=Category_Choice,max_length=5)
    product_image=models.ImageField(upload_to="product")


STATE_CHOICES=(
    ("Andhra Pradesh","Andhra Pradesh"),
    ("Arunachal Pradesh","Arunachal Pradesh"),
    ("Assam","Assam"),
    ("Bihar","Bihar"),
    ("Chhattisgarh","Chhattisgarh"),
    ("Chhattisgarh","Chhattisgarh"),
    ("Goa","Goa"),
    ("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ("Himachal Pradesh","Himachal Pradesh"),
    ("Jammu and Kashmir","Jammu and Kashmir"),
    ("Karnataka","Karnataka"),
    ("Kerala","Kerala"),
    ("Madhya Pradesh","Madhya Pradesh"),
    ("Manipur","Manipur"),
    ("Meghalaya","Meghalaya"),
    ("Mizoram","Mizoram"),
    ("Nagaland","Nagaland"),
    ("Odisa","Odisa"),
    ("Punjab","Punjab"),
    ("Rajasthan","Rajasthan"),
    ("Sikkim","Sikkim"),
    ("Tamil Nadu","Tamil Nadu"),
    ("Telangana","Telangana"),
    ("Tipura","Tipura"),
    ("Uttar Pradesh","Uttar Pradesh"),
    ("Uttarakhand","Uttarakhand"),
    ("West Bengal","West Bengal")
)

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    locality=models.CharField(max_length=50)
    city=models.CharField(max_length=70)
    mobile=models.IntegerField()
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=100)