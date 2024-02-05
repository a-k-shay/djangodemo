from django.shortcuts import render
from django.db.models import Q
from shop.models import Product
# Create your views here.

def search(request):
    b=None
    q=""
    if(request.method=="POST"):
        q=request.POST['q']
        if q:
             b= Product.objects.filter(Q(name__icontains=q)|Q(desc__icontains=q))
    return render(request,'search.html',{'q':q,'p':b})