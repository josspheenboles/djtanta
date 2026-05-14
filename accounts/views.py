from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

from django.views import View
# Create your views here.
def regsiter(request):
    if request.method=='POST':
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render (request,'register.html',
                       {'form':form,'error':form.errors})
    return render (request,'register.html',{'form':UserCreationForm()})

class UserRes(View):
    def get(self,request):
        return render (request,'register.html',{'form':UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'register.html',
                          {'form': form, 'error': form.errors})