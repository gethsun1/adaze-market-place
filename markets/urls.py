from django.urls import path
from django.http import HttpResponse

def markets_home(request):
    return HttpResponse("Welcome to the Markets section!")

urlpatterns = [
    path('', markets_home, name='markets-home'),
]
