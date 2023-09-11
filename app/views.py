from django.shortcuts import render,redirect
from django.views import View
from .models import Product,Customer
from .forms import *
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")

class CategoryView(View):
    def get(self,request,val):
        product=Product.objects.filter(category=val)
        name=Product.objects.filter(category=val).values("name")
        return render(request,"category.html",locals())
class ProductDetail(View):
    def get(self,request,pk):
        pro=Product.objects.get(pk=pk)
        return render(request,"Productdetail.html",locals())
class CategoryTitle(View):
    def get(self,request,val):
        product=Product.objects.filter(name=val)
        name=Product.objects.filter(category=product[0].category).values("name")
        return render(request,"category.html",locals())


class CustomerRegistatinView(View):
    def get(self,request):
        form=CustomerRegistationForm()
        return render(request,"customerregistation.html",locals())
    def post(self,request):
        form=CustomerRegistationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Customer Register Successfully")
            return  redirect("customer-Registation")
        return render(request,"customerregistation.html",locals())


class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,"profile.html",locals())
    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data["name"]
            locality=form.cleaned_data["locality"]
            city=form.cleaned_data["city"]
            mobile=form.cleaned_data["mobile"]
            zipcode=form.cleaned_data["zipcode"]
            state=form.cleaned_data["state"]
            reg=Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,zipcode=zipcode,state=state)
            reg.save()
            messages.success(request,"congratualation profile save succesffully")
            return redirect("profile")
        else:
            messages.warning(request,"invalid input data")
        return render(request,"profile.html",locals())
def Address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request,"address.html",locals())





class Updateaddress(View):
    def get(self,request,pk):
        add=Customer.objects.get(pk=pk)
        form=CustomerProfileForm(instance=add)
        return render(request,"updateaddress.html",locals())
    def post(self,request,pk):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            add=Customer.objects.get(pk=pk)
            add.name=form.cleaned_data["name"]
            add.locality=form.cleaned_data["locality"]
            add.city=form.cleaned_data["city"]
            add.mobile=form.cleaned_data["mobile"]
            add.zipcode=form.cleaned_data["zipcode"]
            add.state=form.cleaned_data["state"]
            add.save()
            messages.success(request,"congratualation profile updated succesffully")
            return redirect("address")
        return render(request,"updateaddress.html",locals())