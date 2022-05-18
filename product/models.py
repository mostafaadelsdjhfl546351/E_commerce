from django.db import models
from unicodedata import name
from statistics import mode
from django.contrib.auth.models import User
# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name
    


class product(models.Model):
    name = models.CharField(max_length=150)
    creator=models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category_id = models.ForeignKey(category,on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name


class Cart(models.Model):
    products_list=models.ManyToManyField(product,null=True,blank=True)
    total=models.IntegerField(default=0)
    date=models.DateTimeField(auto_now_add=False,auto_now=True)
    isPaid=models.BooleanField(default=False)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    def count_cart_items(self):
         return int(self.cart_items)

    def __str__(self) :
        return self.user.username

