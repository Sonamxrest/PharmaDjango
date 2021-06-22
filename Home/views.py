from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def Home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def cart(request):
    return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def contact(request):
    return render(request,'contact.html')
def shop(request):
    return render(request,'shop.html')
def shops(request):
    return render(request,'shop-single.html')
def thankyou(request):
    return render(request,'thankyou.html')

def login(request):
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        user = auth.authenticate(username=un, password=pw)
        if user is not None:
            auth.login(request, user)
            return redirect('../')

    return render(request, 'login.html')
def show_register(request):
    if request.method == 'POST':
        fn = request.POST['fn']
        ln = request.POST['ln']
        em = request.POST['em']
        un = request.POST['un']
        pw = request.POST['pw']
        user = User.objects.create_user(first_name=fn,
        last_name=ln, email=em, username=un, password=pw)
        user.save()

    return render(request, 'register.html')


@login_required
def do_logout(request):
    auth.logout(request)
    return redirect('../login')