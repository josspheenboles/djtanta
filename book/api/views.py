from django import views
from django.http import JsonResponse
from book.models import *
def json(request):
    books=Book.objects.values('id','title')
    return JsonResponse(list(books),safe=False)