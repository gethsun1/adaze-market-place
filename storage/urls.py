from django.urls import path
from django.http import HttpResponse

def storage_home(request):
    return HttpResponse("Welcome to the Storage section!")

urlpatterns = [
    path('', storage_home, name='storage-home'),
]
