from django.urls import path

from Medicine import views

urlpatterns = [
    path('show',views.show_medicine),
    path('mycart', views.my_medicine),
    path('mycart/<mid>', views.add_to_cart)
         ]