from django.shortcuts import render,redirect
from django.http.response import HttpResponse,HttpResponseRedirect
from pip._internal import req

from .models import *
# Create your views here.
#view is function---->httprequest as param & return object of httprespone
def listbook(request):
    # return HttpResponse('<h1>Book List</h1>')

    context={'title':'tanta demo','books':Book.objects.all()}

    return render(request,'book/list.html',context)
def getbookbyid(request,id):
    # return HttpResponse(f'<h1>book detaild nu,ber {id}</h1>')
    #get book
    context={'book':Book.objects.get(id=id)}
    #render
    return render(request,'book/bookdetails.html',context)
def bookupdate(req,id):
    return HttpResponse(f'<h1>book update for id:{id}</h1>')
def bookdelete(req,id):
    return HttpResponse(f'<h1>book Delete for id:{id}</h1>')
def newbook(request):
    context = {'catagories': Catagory.objects.all()}
    # return HttpResponse(f'<h1>book add</h1>')
    if request.method == 'POST':

        Book.objects.create(
            title=request.POST['title'],
            description=request.POST['decrption'],
            price=request.POST['price'],
            image=request.FILES.get("image")
        )
        # return HttpResponseRedirect('/Book/')
        return redirect ('Booklist')

    return render (request,'book/new.html',context)

def getbookbyname(request,name):
    print(request.get_host())
    # print('GET dict',request.GET,'POST dict',request.POST)
    objresponse=HttpResponse(f'<h1>get book  by Name: {name}</h1>')
    objresponse.write('added respons')
    # objresponse['content-type']='text/plain'
    return  objresponse

def Hardbookdelete(request,id):
    #check if id ok
    if (Book.objects.filter(pk=id) ):
        #delete
        Book.objects.filter(id=id).delete()
        #redirect book list
        return redirect('Booklist')
    # else:
    else:
        return render(request,'book/list.html',context={'error':'book not found'})
    #     return error