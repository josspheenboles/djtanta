from django import views
from django.http import JsonResponse,HttpResponse
from book.models import *

def json(request):
    # print(Book.objects.all())
    books=Book.objects.values('id','title')
    # print(Book.objects.values('id','title'))
    return JsonResponse(list(books),safe=False)