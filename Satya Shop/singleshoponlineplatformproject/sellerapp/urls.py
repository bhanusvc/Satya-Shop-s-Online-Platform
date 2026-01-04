from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
        path('sellerloginpage',views.sellerloginpage,name="sellerloginpage"),
        path('sellerlogin',views.sellerlogin,name="sellerlogin"),
        path('sellerlogout',views.sellerlogout,name="sellerlogout"),
        path('sellerhome',views.sellerhomepage,name="sellerhome"),
        path("additems", views.additemspage, name="additems"),
        path("listitems", views.listitemspage, name="listitems"),
        path("edititems", views.edititemspage, name="edititems"),
        path("orders", views.sellerorderspage, name="sellerorders"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)