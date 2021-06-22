from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Medicine.models import Medicine, Cart



def show_medicine(request):
    if request.method == 'POST':
        qty = request.POST['qty']
        mid = request.POST['mid']
        med = Medicine.objects.get(pk=mid)
        av = med.stock
        if int(qty) > med.stock:
            return HttpResponse('Out of stock')
        else:
            cart = Cart(medicine=med,user=request.user,qty=qty,date=datetime.now())
            cart.save()
            new_stock = int(av)-int(qty)
            med.stock(new_stock)
            med.save()
            return HttpResponse('Your order added to your cart')
    medicines = Medicine.objects.all()
    return render(request, 'shop.html', {'mbs': medicines})

@login_required
def add_to_cart(request, mid):
    user = request.user
    medicine = Medicine.objects.get(id=mid)
    date = datetime.now()
    cart = Cart(user=user, medicine=medicine, date=date)
    cart.save()
    return HttpResponse('<script>alert("Added to cart")</script>')


def my_medicine(request):
    cart = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart': cart})

