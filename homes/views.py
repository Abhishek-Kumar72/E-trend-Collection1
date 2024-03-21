from django.shortcuts import render
from homes.models import SignupUser
from django.contrib.auth.hashers import make_password
from homes.models import Payment

# Create your views here.



def index(request):
    return render(request, 'homes/ecommerce.html')
def login(request):
    return render(request,'homes/login.html',{'title':'login'})
def signup(request):
    if request.method == "POST":
        un =request.POST.get('name')
        em =request.POST.get('email')
        pn =request.POST.get('pno')
        Ad =request.POST.get('Address')
        p1 =request.POST.get('psw1')    
        p2 =request.POST.get('psw2')

        user_exist = SignupUser.objects.filter(username=un)
        if user_exist:
            context = {'msg':'user already exist'}
            return render(request,'homes/signup.html',context)
        else:
            # print("++++>>")
            data = SignupUser(
                username = un,
                email =em,
                phonenumber =pn,
                Address=Ad,
                password= make_password(p1),
                reenterpassword=make_password(p2))
            data.save()
            context ={'msg':'user REgistered Successfully'}
            return render(request,'homes/signup.html',context)
        
    else:
         return render(request,'homes/signup.html',{'title':'signup'})

def forget(request):
    return render(request,'homes/forget.html',{'title':'forget'})
def payment(request):
    if request.method == "POST":
        fn =request.POST.get('Fullname')
        em =request.POST.get('Email')
        Ad =request.POST.get('Address')
        ct =request.POST.get('City')
        zc=request.POST.get('Zipcode')    
        cn =request.POST.get('Cardnumber')
        em =request.POST.get('Expmonth')
        cv =request.POST.get('Cvv')

        user_exist = Payment.objects.filter(Fullname=fn)
        if user_exist:
            context = {'msg':'user already exist !'}
            return render(request,'homes/payment.html',context)
        else:
            # print("++++>>")
            data = Payment(
                Fullname = fn,
                Email =em,
                Address =Ad,
                City=ct,
                Zipcode=zc,
                Cardnumber=cn,
                Expmonth=em,
                Cvv=cv)
                
            data.save()
            context ={'msg':'user REGISTER Successfully !'}
            return render(request,'homes/payment.html',context)
        
    else:
        return render(request,'homes/payment.html',{'title':'payment'})
def shoes(request):
    return render(request,'homes/shoes.html',{'title':'shoes'})
def hoodies(request):
    return render(request,'homes/hoodies.html',{'title':'hoodies'})
def jeans(request):
    return render(request,'homes/jeans.html',{'title':'jeans'})
def watch(request):
    return render(request,'homes/watch.html',{'title':'watch'})
def smartphone(request):
    return render(request,'homes/smartphone.html',{'title':'smartphone'})
def television(request):
    return render(request,'homes/television.html',{'title':'television'})
def TShirt(request):
    return render(request,'homes/TShirt.html',{'title':'TShirt'})
def dinnerset(request):
    return render(request,'homes/dinnerset.html',{'title':'dinnerset'})
def blankets(request):
    return render(request,'homes/blankets.html',{'title':'blankets'})
def laptop(request):
    return render(request,'homes/laptop.html',{'title':'laptop'})
def microwave(request):
    return render(request,'homes/microwave.html',{'title':'microwave'})
def coffeemaker(request):
    return render(request,'homes/coffeemaker.html',{'title':'coffeemaker'})
def bed(request):
    return render(request,'homes/bed.html',{'title':'bed'})
def Airconditioner(request):
    return render(request,'homes/Airconditioner.html',{'title':'signup'})
def book(request):
    return render(request,'homes/book.html',{'title':'book'})
def bag(request):
    return render(request,'homes/bag.html',{'title':'bag'})
def sarees(request):
    return render(request,'homes/sarees.html',{'title':'sarees'})
def washingmachine(request):
    return render(request,'homes/washingmachine.html',{'title':'washingmachine'})
def addtocart(request):
    return render(request,'homes/addtocart.html',{'title':'addtocart'})
def contact(request):
    return render(request,'homes/contact.html',{'title':'contact'})

