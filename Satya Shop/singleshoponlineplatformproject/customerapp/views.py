from django.http import request
from django.shortcuts import render

# Create your views here.
def customerregisterpage(request):
    return render(request,"customer/customerregister.html")
def customerloginpage(request):
    return render(request, "customer/customerlogin.html")

