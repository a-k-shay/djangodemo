from django.shortcuts import render, redirect
from shop.models import Category,Product
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.


def allcategories(request):
    c=Category.objects.all()
    return render(request,"category.html", context={'c': c})

def product(request,p):
    c=Category.objects.get(name=p)
    p=Product.objects.filter(category=c)
    return render(request,'product.html',{'c':c,'p':p})


def details(request,p):
    p=Product.objects.get(name=p)
    return render(request,'details.html',{'p':p})


def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:allcat')
        else:
            return HttpResponse("invalid credentials")

    return render(request,'login.html')


def register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e= request.POST['e']
        fname = request.POST['f']
        lname = request.POST['l']

        if(p==cp):
            user= User.objects.create_user(username=u,password=p,first_name=fname,last_name=lname,email=e)
            user.save()
            return redirect('shop:allcat')
        else:
            return HttpResponse('p r not same' )
    return render(request,'register.html')

@login_required
def user_logout(request):
    logout(request)
    return user_login(request)
