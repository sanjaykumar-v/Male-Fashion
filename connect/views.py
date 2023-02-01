from django.contrib.auth import authenticate, login,logout
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import  User

from connect.models import Admins, Category, Productss,contacts


# Create your views here.
def home(req):
    return render(req,"index.html")

def add_admin(req):
    return render(req,"add_admin.html")

def save_admin(req):
    data=Admins.objects.all()

    if req.method == "POST":
        na=req.POST.get('name')
        mob = req.POST.get('mob')
        em = req.POST.get('email')
        us = req.POST.get('user')
        pw = req.POST.get('pwd')
        cp = req.POST.get('con')
        im = req.FILES['img']
        obj =Admins(Name=na, Mobile=mob, Email=em, Username=us, Password=pw, Confirm=cp, Image=im)
        obj.save()
    return render(req,'add_admin.html',{'data': data})

def display_admins(req):
    data = Admins.objects.all()
    return render(req, "view_admin.html", {'data': data})

def edt_adm(req, dataid):
    data = Admins.objects.get(id=dataid)
    print(data)
    return render(req, "edit_admin.html", {'data': data})

def update_admin(req,dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        mob = req.POST.get('mob')
        em = req.POST.get('email')
        us = req.POST.get('user')
        pw = req.POST.get('pwd')
        cp = req.POST.get('con')
        try:
            im = req.FILES['img']
            fs = FileSystemStorage()
            file= fs.save(im.name,im)
        except MultiValueDictKeyError:
            file = Admins.objects.get(id=dataid).Image
        Admins.objects.filter(id=dataid).update(Name=na, Mobile=mob, Email=em, Username=us, Password=pw, Confirm=cp, Image=file)
        return redirect(display_admins)

def delete_admin(req,dataid):
    data = Admins.objects.filter(id=dataid)
    data.delete()
    return redirect(display_admins)

def add_catg(req):
    return render(req,"add_category.html")

def save_categ(req):
    if req.method == "POST":
        na = req.POST.get('name')
        de = req.POST.get('desc')
        im = req.FILES['img']
        obj = Category(Name=na, Description=de, Image=im)
        obj.save()
        return redirect(add_catg)

def display_categ(req):
    data = Category.objects.all()
    return render(req, "view_category.html", {'data': data})

def edit_categ(req, dataid):
    data = Category.objects.get(id=dataid)
    print(data)
    return render(req, "edit_category.html", {'data': data})

def update_categ(req, dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        de = req.POST.get('desc')
        try:
            im = req.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = Category.objects.get(id=dataid).Image
        Category.objects.filter(id=dataid).update(Name=na, Description=de, Image=file)
        return redirect(display_categ)

def delete_categ(req, dataid):
    data = Category.objects.filter(id=dataid)
    data.delete()
    return redirect(display_categ)


def add_prod(req):
    data = Category.objects.all()
    return render(req, "add_product.html", {'data': data})

def save_prod(req):
    if req.method == "POST":
        na = req.POST.get('name')
        pr = req.POST.get('price')
        bd = req.POST.get('Brand')
        de = req.POST.get('desc')
        im = req.FILES['img']
        cat = req.POST.get('categ')
        obj = Productss(Name=na, Price=pr, Brand=bd, Description=de, Image=im, Categry=cat)
        obj.save()
        return redirect(add_prod)

def display_prod(req):
    data = Productss.objects.all()
    return render(req, "view_products.html", {'data': data})

def edit_prod(req, dataid):
    data = Productss.objects.get(id=dataid)
    da = Category.objects.all()
    return render(req, "edit_products.html", {'data': data, 'da': da})


def update_prod(req, dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        pr = req.POST.get('price')
        bd = req.POST.get('Brand')
        de = req.POST.get('desc')
        cat = req.POST.get('categ')
        try:
            im = req.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = Productss.objects.get(id=dataid).Image
        Productss.objects.filter(id=dataid).update(Name=na, Price=pr, Brand=bd, Description=de, Image=file, Categry=cat)
        return redirect(display_prod)


def delete_prod(req, dataid):
    data = Productss.objects.filter(id=dataid)
    data.delete()
    return redirect(display_prod)

def show(req):
    return render(req, "test.html")

def log(req):
    return render(req, "login.html")


def adminlog(req):
    if req.method == "POST":
        user_r = req.POST.get('user')
        pwd_r = req.POST.get('pwd')

        if User.objects.filter(username__contains=user_r).exists():
            us = authenticate(username=user_r, password=pwd_r)

            if us is not None:
                login(req, us)
                req.session['username'] = user_r
                req.session['password'] = pwd_r
                return redirect(home)

            else:
                return redirect(log)

        else:
            return redirect(log)

def display_contacts(req):
    data = contacts.objects.all()
    return render(req, "customer_contact.html", {'data': data})

def llogout(request):
    logout(request)
    return redirect(log)