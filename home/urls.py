from django.contrib import admin
from django.urls import path 
from home import views

admin.site.site_header = "DMP CLOTHING"
admin.site.site_title = "DMP Admin Portal"
admin.site.index_title = "Welcome to DMP Admin Portal"


urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services'),
    path('checkout',views.checkout,name='checkout'),
    path('jeans',views.jeans,name='jeans'),
    path('Shirts',views.Shirts,name='Shirts'),
    path('TShirts',views.TShirts,name='T-Shirts'),

]
