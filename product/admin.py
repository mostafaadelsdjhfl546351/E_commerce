from django.contrib import admin
from .models import Cart, category,product
# Register your models here.
admin.site.register(category)
admin.site.register(product)
admin.site.register(Cart)