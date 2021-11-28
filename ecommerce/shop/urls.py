from django.contrib import admin
from django.urls import path,include
from . import views

app_name='shop'

urlpatterns = [
    path('',views.AllProductCat,name='AllProductCat'),
    path('product_by_cat/<slug:c_slug>/',views.AllProductCat,name='product_by_cat'),
    path('productdetailcat/<slug:c_slug>/<slug:product_slug>/',views.ProductDetail,name='productdetailcat'),

]

