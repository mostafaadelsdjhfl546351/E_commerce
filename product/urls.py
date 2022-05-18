
from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('cats',views.AllCategories,name="cats"),
    path('category/<int:categoryid>/',views.Category,name="Category"),
    path('product/<int:productid>/',views.Product,name="Product"),
    path('cart/<int:userId>', views.cart_view, name='list_cart'),
    # path('cart/create/', views.create, name='create_cart'),
    # path('cart/detail/<int:product_id>/', views.detail, name='detail_cart'),
    path('cart/update/<int:product_id>/', views.update_cart, name='update_cart'),
]