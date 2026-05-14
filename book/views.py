from django.shortcuts import render,redirect
from django.http.response import HttpResponse,HttpResponseRedirect
from pip._internal import req
from django.views import View
from django.views.generic import ListView

from .models import *
from .forms import *

class BookList(ListView):

    queryset = Book.objects.filter(is_active=True)
    model=Book
    template_name = 'book/list.html'
    context_object_name = 'books'

# Create your views here.
#view is function---->httprequest as param & return object of httprespone
def listbook(request):
    # return HttpResponse('<h1>Book List</h1>')
    # request.session.pop('info')
    context={'title':'tanta demo','books':Book.objects.filter(is_active=True)}

    return render(request,'book/list.html',context)
def getbookbyid(request,id):
    # return HttpResponse(f'<h1>book detaild nu,ber {id}</h1>')
    #get book
    context={'book':Book.objects.get(id=id)}
    #render
    return render(request,'book/bookdetails.html',context)
def bookupdate(req,id):
    oldobj=Book.objects.get(pk=id)
    if req.method=='POST':
        form=BookFormModel(data=req.POST,files=req.FILES,instance=oldobj)
        if form.is_valid():
            form.save()#update
            return redirect('Booklist')
        else:
            return render(req, 'book/update.html', {'form': form,'errors':form.errors})
    #get
    return render(req,'book/update.html',{'form':BookFormModel(instance=oldobj)})
def bookdelete(req,id):
    return HttpResponse(f'<h1>book Delete for id:{id}</h1>')
class BookNew(View):
    context = {'catagories': Catagory.objects.all(), 'form': BookFormModel()}
    def get(self,request):
        return render(request, 'book/new.html', BookNew.context)
    def post(self,request):
        form = BookFormModel(data=request.POST, files=request.FILES)
        if (form.is_valid()):
            form.save()
            # Book.objects.create(
            #     title=request.POST['title'],
            #     description=request.POST['decrption'],
            #     price=request.POST['price'],
            #     image=request.FILES.get("image"),
            #     Catagory=Catagory.objects.get(pk=request.POST['catagory'])
            # )
        # return HttpResponseRedirect('/Book/')
        request.session['info'] = 'bookadded'
        request.session['username'] = 'hamada'
        return redirect('Booklist')


def newbook(request):
    context = {'catagories': Catagory.objects.all(),'form':BookFormModel()}
    # return HttpResponse(f'<h1>book add</h1>')
    if request.method == 'POST':
        form=BookFormModel(data=request.POST,files=request.FILES)
        if(form.is_valid()):
            form.save()
            # Book.objects.create(
            #     title=request.POST['title'],
            #     description=request.POST['decrption'],
            #     price=request.POST['price'],
            #     image=request.FILES.get("image"),
            #     Catagory=Catagory.objects.get(pk=request.POST['catagory'])
            # )
        # return HttpResponseRedirect('/Book/')
        request.session['info']='bookadded'
        request.session['username']='hamada'
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

def softbookdelete(request,id):
    Book.objects.filter(pk=id).update(is_active=False)
    print(Book.objects.filter(pk=id).first().is_active)
    return redirect('Booklist')