from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import Book
# Create your views here.
def home(request):
    if(request.method=='POST'):
        name=request.POST['name']
        number=request.POST['number']   
        email=request.POST['email']
        subject=request.POST['subject']
        time=request.POST['time']
        
        pst=Book.objects.create(Name=name,Number=number,Email=email,Time=time,Subject=subject)
        pst.save()
        return render(request,"index.html",{"name":name})
    else:
        return render(request,"index.html")
def programming(request):
    return render(request,"programming.html")