from django.shortcuts import render

def landingpage(request):
    return render(request,"index.html")
def homepage(request):
    return render(request,"home.html")
def aboutpage(request):
    return render(request,"about.html")
def contactpage(request):
    return render(request,"contactandfaq.html")
def catalogpage(request):
    return render(request,"catalog.html")