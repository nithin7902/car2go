from django.shortcuts import render,redirect
from . models import *
# Create your views here.
def seller_login (request):
    if request.method=='POST':
        Email=request.POST['email']
        Password=request.POST['password']
        try:
            sell=SellerRegistration.objects.get(email=Email,password=Password)
            request.session['seller']=sell.id
            return redirect('seller:seller_dashboard')
        except SellerRegistration.DoesNotExist:
            return render(request,'seller/seller_login.html',{'msg':'invalid username or password'})
    return render(request,'seller/seller_login.html')
def seller_home (request):
    return render(request,'seller/seller_home.html')

def seller_dashboard (request):
    if 'seller' in request.session:
        seller_id = request.session.get('seller')
        cust=SellerRegistration.objects.get(id=seller_id)
        customer=cust.email
        firstletter=customer[0]
        # firstletter=firstletter.upper()
        return render(request,'seller/seller_dashboard.html',{'firstletter':firstletter})

def addproduct (request):
    if request.method=='POST':
        car_name=request.POST['name']
        car_brand=request.POST.get('brand')
        car_color=request.POST.get('color') 
        rent_charge=request.POST.get('charge')
        Image=request.FILES['image']
        topspeed=request.POST.get('speed')
        capacity=request.POST.get('capacity')
        fuels=request.POST.get('fuels')
        product=Products(car_name=car_name,car_brand=car_brand,car_color=car_color,rent_charge=rent_charge,image=Image,topspeed=topspeed,capacity=capacity,fuels=fuels)
        product.save()
        return redirect('seller:seller_views')
    return render(request,'seller/addproduct.html')

def seller_views (request):
    product=Products.objects.all()
    return render(request,'seller/seller_views.html',{'products':product})

def delete_product(request,product_id):
    Products.objects.get(id=product_id).delete()
    return redirect('seller:seller_views')
def update_product(request,product_id):
    car=Products.objects.get(id=product_id)
    if request.method=='POST':
        car_name=request.POST['name']
        car_brand=request.POST.get('brand')
        car_color=request.POST.get('color') 
        rent_charge=request.POST.get('charge')
        topspeed=request.POST.get('speed')
        capacity=request.POST.get('capacity')
        fuels=request.POST.get('fuels')
        try:
            Image=request.FILES['image']
            car.image=Image
        except:
            car.image=car.image
        car.car_name=car_name
        car.car_brand=car_brand
        car.car_color=car_color
        car.rent_charge=rent_charge
        car.topspeed=topspeed
        car.capacity=capacity
        car.fuels=fuels
        car.save()
        return redirect('seller:seller_views')
    return render(request,'seller/car_update.html',{'car':car})
def seller_logout(request):
    if 'seller' in request.session:
        del request.session['seller']
        return render(request,'seller/seller_home.html')
    else:
        return render (request,'seller/seller_home.html')
    
def index (request):
    return render(request,'customer/index.html')    