from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
        path('customerlogin',views.customerloginpage,name="cusotmerlogin"),
        path('customerregistration',views.customerregisterpage,name="customerregistration"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)