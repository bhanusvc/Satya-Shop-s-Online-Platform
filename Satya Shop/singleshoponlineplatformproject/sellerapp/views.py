from django.shortcuts import render

# Create your views here.
def sellerloginpage(request):
    return render(request,"seller/sellerlogin.html")