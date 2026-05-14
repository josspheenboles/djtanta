from django.urls import path,include
from book.views import *
from .views import *
urlpatterns = [
    path('json/',json)
    ]