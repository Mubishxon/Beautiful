from django.urls import path
from .views import asosiypage,about,client,contact,products

urlpatterns =[
    path('', asosiypage, name = 'index'),
    path('about/', about, name = 'about'),
    path('client/', client, name ='client'),
    path('contact/',contact, name ='contact'),
    path('products/',products, name = 'products')
]
