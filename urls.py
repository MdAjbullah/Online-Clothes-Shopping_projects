
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home/', views.home),
    path('createaccount/', views.createaccount),
    path('login/', views.loginform),
    path('logindata/', views.logindata),
    path('admin1/', views.admin1),
    path('addproduct/', views.addproduct),
    path('registerproduct/', views.registerproduct),
    path('showproduct/', views.showproduct),
    path('deletepro/<int:pk>/', views.deletepro, name="deletepro"),
    path('showuser/', views.showuser),
    path('logout/', views.logout),
    path('registerdata/', views.registerdata),
    path('user/', views.user),
    path('deleteuser/<int:pk>/', views.deleteuser, name="deleteuser"),
    path('myordershow/', views.myordershow),
    path('addoffer/', views.addoffer),
    path('addofferdata/', views.addofferdata),
    path('showoffer/', views.showoffer),
    path('deleteoffer/<int:pk>/', views.deleteoffer, name="deleteoffer"),
    path('usershowproduct/', views.usershowproduct),
    path('final/', views.final),
    path('myorder/', views.myordershow),
    path('updatestatus/<int:pk>/', views.updatestatus, name="updatestatus"),
    path('deleteorder/<int:pk>/', views.deleteorder, name="deleteorder"),
    path('userorder/', views.userorder),
    path('accountsetting/', views.accountsetting),
    path('accountsetting1/', views.accountsetting1),
    path('showdetail/<int:pk>/', views.showdetail, name="showdetail"),
    path('saverating/', views.saverating),
    path('deletemyproduct/<int:pk>/', views.deletemyproduct, name="deletemyproduct"),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
