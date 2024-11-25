from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Adaze Marketplace!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Root URL
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('transporters/', include('transporters.urls')),
    path('storage/', include('storage.urls')),
    path('markets/', include('markets.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]
