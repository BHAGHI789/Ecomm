from django.contrib import admin

# Register your models here.
from .models import Product,Customer
class ProductAdmin(admin.ModelAdmin):
    list_display=["id","name","selling_price","discounted_price","discription","compsition","category","product_image"]
admin.site.register(Product,ProductAdmin)

class Customeradmin(admin.ModelAdmin):
    list_display=["id","user","name","locality","city","mobile","zipcode","state"]
admin.site.register(Customer,Customeradmin)