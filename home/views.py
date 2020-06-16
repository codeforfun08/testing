from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import Book
from django.core.mail import send_mail
# Create your views here.
def home(request):
    if(request.method=='POST'):
        name=request.POST['name']
        number=request.POST['number']   
        email=request.POST['email']
        subject=request.POST['subject']
        time=request.POST['time']
        details='Thank You For Booking the Demo Session\n'+'Details:\n'+name+'\n'+number+'\n'+email+'\n'+subject+'\n'+time
        send_mail(
            'Welcome To Philomath',
            details,
            'philomathclasses@gmail.com',
            [email],
        )
        pst=Book.objects.create(Name=name,Number=number,Email=email,Time=time,Subject=subject)
        pst.save()
        return render(request,"index.html",{"name":name,"details":details})
    else:
        return render(request,"index.html")
       
def webdev(request):
    return render(request,"webdev.html")


def programming(request):
    return render(request,"programming.html")