from django.shortcuts import render
from .models import category,product,Cart
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.
from . import views

def home(request):
    allcategory = category.objects.all()
    allproducts = product.objects.all()
    return render(request,'pages/home.html',{"allproducts":allproducts,"allcategory":allcategory})

def Category(request,categoryid):
    allcategory = category.objects.all()
    mycategory = category.objects.get(id=categoryid)
    allproducts = product.objects.all().filter(category_id = categoryid )
    return render(request,'pages/product_list.html',{"allproducts":allproducts,"allcategory":allcategory,"mycategory":mycategory})

def Product(request,productid):
    allcategory = category.objects.all()
    myproduct = product.objects.get(id=productid)
    return render(request,'pages/product.html',{"allcategory":allcategory,"myproduct":myproduct})

def AllCategories(request):
    allcategory = category.objects.all().order_by("-id")
    return render(request,'pages/category.html',{"allcategory":allcategory})

def cart_view(request, userId):
    cart_owner=User.objects.filter(id=userId)[0]
    cart=Cart.objects.filter(user=cart_owner)[0]
    print(cart)
    return render(request,'pages/cart.html',{'cart':cart})

def update_cart(request,product_id):
    cart=Cart.objects.all()[0]
    try:
        product1=product.objects.get(id=product_id)
    except product.DoesNotExist:
        pass
    if not product1 in cart.products_list.all():
        cart.products_list.add(product1)
    else:
        cart.products_list.remove(product1)
    return HttpResponseRedirect("cart")
