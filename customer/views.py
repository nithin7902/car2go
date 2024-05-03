from django.shortcuts import render,redirect
from . models import *
from seller.models import Products
from django.http import HttpResponse
# Create your views here.
def index (request):
    return render(request,'customer/index.html')
def login (request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        try:
            cust=Customer.objects.get(email=email,password=password)
            request.session['customer']=cust.id
            return redirect('customer:rentcar')
        except Customer.DoesNotExist:
            return render(request,'customer/login.html',{'msg':'invalid username or password'})
    return render(request,'customer/login.html')
def signup (request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['number']
        email=request.POST['email']
        password=request.POST['password']
        customer=Customer(name=name,phone=phone,email=email,password=password)
        customer.save()
        return redirect('customer:login')
    return render(request,'customer/signup.html')
def rentcar (request):
    if 'customer' in request.session:
        customer_id = request.session.get('customer')
        cust=Customer.objects.get(id=customer_id)
        customer=cust.name
        firstletter=customer[0]
        customer
        # firstletter=firstletter.upper()
        products=Products.objects.all()
        return render(request,'customer/rentcar.html',{'products':products,'firstletter':firstletter})
    else:
        return render (request,'customer/index.html')
def contactus (request):
    return render(request,'customer/contact.html')
def about (request):
    return render(request,'customer/about.html')
def viewdetails (request,car_id):
    if 'customer' in request.session:
        customer_id = request.session.get('customer')
        cust=Customer.objects.get(id=customer_id)
        customer=cust.name
        firstletter=customer[0]
        # firstletter=firstletter.upper()
        car=Products.objects.get(id=car_id)
        return render(request,'customer/viewdetails.html',{'car':car ,'firstletter':firstletter})
    else:
        return render (request,'customer/index.html')
def payment (request):
    if 'customer' in request.session:
        
        return render(request,'customer/payment.html')
    else:
        return render (request,'customer/index.html')
def logout (request):
    if 'customer' in request.session:
        del request.session['customer']
        return render(request,'customer/index.html')
    else:
        return render (request,'customer/index.html')

