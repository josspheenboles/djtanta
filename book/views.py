from django.shortcuts import render
from django.http.response import HttpResponse
from .models import *
# Create your views here.
#view is function---->httprequest as param & return object of httprespone
def listbook(request):
    # return HttpResponse('<h1>Book List</h1>')

    context={'title':'tanta demo','books':Book.objects.all()}

    return render(request,'book/list.html',context)
def getbookbyid(request,id):
    return HttpResponse(f'<h1>book detaild nu,ber {id}</h1>')
def bookupdate(req,id):
    return HttpResponse(f'<h1>book update for id:{id}</h1>')
def bookdelete(req,id):
    return HttpResponse(f'<h1>book Delete for id:{id}</h1>')
def newbook(request):
    return HttpResponse(f'<h1>book add</h1>')

def getbookbyname(request,name):
    print(request.get_host())
    # print('GET dict',request.GET,'POST dict',request.POST)
    objresponse=HttpResponse(f'<h1>get book  by Name: {name}</h1>')
    objresponse.write('added respons')
    # objresponse['content-type']='text/plain'
    return  objresponse

