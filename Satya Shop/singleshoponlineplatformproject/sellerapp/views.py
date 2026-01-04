from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Seller


# Create your views here.
def sellerloginpage(request):
    return render(request,"seller/sellerlogin.html")

def sellerlogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("password")

        try:
            seller = Seller.objects.get(username=username)

            if seller.password == pwd:
                request.session["seller_id"] = seller.id
                request.session["seller_name"] = seller.shop_name
                return redirect("sellerhome")
            else:
                messages.error(request, "Invalid password")

        except Seller.DoesNotExist:
            messages.error(request, "Invalid username")

    return redirect("sellerloginpage")

def sellerhomepage(request):
    if "seller_id" not in request.session:
        return redirect("sellerloginpage")
    return render(request, "seller/sellerhome.html")