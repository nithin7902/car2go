from django.urls import path
from . import views
app_name='customer'
urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('rentcar/',views.rentcar,name='rentcar'),
    path('contactus/',views.contactus,name='contactus'),
    path('about/',views.about,name='about'),
    path('viewdetails/<int:car_id>',views.viewdetails,name='viewdetails'),
    path('payment/',views.payment,name='payment'),
    path('logout/',views.logout,name='logout')
]