from django.urls import path

from Home import views

urlpatterns=[
path('',views.Home),
path('about',views.about),
path('cart',views.cart),
path('checkout',views.checkout),
path('shop',views.shop),
path('shop-single',views.shops),
path('thankyou',views.thankyou),
    path('login',views.login),
    path('register',views.show_register),
    path('logout',views.do_logout),
    path('contact',views.contact)



]