from django.shortcuts import render, redirect
from connect.models import Category, contacts, Productss
from menapp.models import Customerdetails
from django.contrib.auth import  authenticate,logout


# Create your views here.

def home_pg(req):
    data = Category.objects.all()
    return render(req, "home.html", {'data': data})

def about_pg(req):
    data = Category.objects.all()
    return render(req, "about.html", {'data': data})

def contact_pg(req):
    data = Category.objects.all()
    return render(req, "contact.html", {'data': data})

def contacts1(req):
    if req.method == "POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        msg = req.POST.get('message')
        obj = contacts(Name=na, Email=em, message=msg)
        obj.save()
        return redirect(contact_pg)

def products_pg(req):
    data = Productss.objects.all()
    return render(req, "products.html", {'data': data})

def dispCateg(req, itemCateg):
    # data=Category.object.all()
    print("===itemCateg===", itemCateg)
    catg = itemCateg.upper()
    products = Productss.objects.filter(Categry=itemCateg)
    context = {
        'products': products,
        'catg': catg,
        # 'data':data
    }
    return render(req, "displayCategory.html", context)

def displayProd(req, dataid):
    data = Productss.objects.get(id=dataid)
    return render(req, "productDetails.html", {'data': data})


def login(request):
    return render(request, "login_or_register.html")

def loginsave(request):
    if request.method == "POST":
        u = request.POST.get('user')
        e = request.POST.get('email')
        p = request.POST.get('pass')
        c = request.POST.get('cpass')
        if p == c:
            obj = Customerdetails(username=u, email=e, password=p, confirmpassword=c)
            obj.save()
            return redirect(login)
        else:
            return render(request, 'login_or_register.html', {'msg': "Sorry......password not matched "})

def Customer_login(request):
    if request.method == 'POST':
        u = request.POST.get("user")
        p = request.POST.get("pass")

        if Customerdetails.objects.filter(username=u, password=p).exists():
            request.session['user'] = u
            request.session['pass'] = p
            return redirect(home_pg)
        else:
            return render(request, "login_or_register.html", {'msg': "Sorry......password not matched "})

def llogout(request):
    logout(request)
    return redirect(home_pg)