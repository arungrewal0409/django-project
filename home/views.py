from multiprocessing import context
from django.shortcuts import render,HttpResponse
from home.models import checkout
from datetime import datetime
# Create your views here.
def index(request):
    context = {'variable':'i am great'
    }
    return render(request,"index.html",context)
    #return HttpResponse("this is homepage")
 
def about(request):
    return render(request,"about.html")
    # return HttpResponse("this is about page")
 
def services(request):
    return render(request,"services.html")
   #return HttpResponse("this is services page")
 
def contact(request):
    return render(request,"contact.html")

def checkout(request):
    
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        Username=request.POST.get('Username')
        Email=request.POST.get('Email')
        Address=request.POST.get('Address')
        Address2=request.POST.get('Address2')
        Name_on_card=request.POST.get('Name_on_card') 
        Credit_card_number=request.POST.get('Credit_card_number')
        Expiration=request.POST.get('Expiration') 
        CVV=request.POST.get('CVV')  

        Checkout =checkout (first_name=first_name, last_name=last_name, Username= Username, Email=Email, Address=Address, Address2=Address2,Name_on_card=Name_on_card, Credit_card_number=Credit_card_number, Expiration=Expiration, CVV=CVV, date=datetime.today())
        checkout.save()
    
    return render(request,"checkout.html")

def jeans(request):
    return render(request,"jeans.html")

def Shirts(request):
    return render(request,"Shirts.html")

def TShirts(request):
    return render(request,"T-Shirts.html")      
 