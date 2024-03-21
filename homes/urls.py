from django.urls import path
from homes import views

urlpatterns = [
    path('', views.index, name="homes-ecommerce"),
    path('login/', views.login , name="homes-login"),
    path('signup/',views.signup, name="homes-signup"),
    path('forget/',views.forget, name="homes-forget"),
    path('payment/',views.payment, name="homes-payment"),
    path('shoes/',views.shoes, name="homes-shoes"),
    path('hoodies/',views.hoodies, name="homes-hoodies"),
    path('jeans/',views.jeans, name="homes-jeans"),
    path('watch/',views.watch, name="homes-watch"),
    path('smartphone/',views.smartphone, name="homes-smartphone"),
    path('television/',views.television, name="homes-television"),
    path('TShirt/',views.TShirt, name="homes-TShirt"),
    path('dinnerset/',views.dinnerset, name="homes-dinnerset"),
    path('blankets/',views.blankets, name="homes-blankets"),
    path('laptop/',views.laptop, name="homes-laptop"),
    path('microwave/',views.microwave, name="homes-microwave"),
    path('coffeemaker/',views.coffeemaker, name="homes-coffeemaker"),
    path('bed/',views.bed, name="homes-bed"),
    path('Airconditioner/',views.Airconditioner, name="homes-Airconditioner"),
    path('book/',views.book, name="homes-book"),
    path('bag/',views.bag, name="homes-bag"),
    path('sarees/',views.sarees, name="homes-sarees"),
    path('washingmachine/',views.washingmachine, name="homes-washingmachine"),
    path('addtocart/',views.addtocart, name="homes-addtocart"),
    path('contact/',views.contact,name="homes-contact"),
    

]
