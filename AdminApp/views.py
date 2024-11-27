from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from AdminApp.models import Category, Product
from WebApp.models import Contacts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def IndexPage(request):
    cat = Category.objects.count()
    pro = Product.objects.count()
    con = Contacts.objects.count()
    return render(request, "index.html", {'cat':cat, 'pro':pro, 'con':con})

def CustomerContacts(request):
    contacts = Contacts.objects.all()
    return render(request, "DisplayContact.html", {'contacts':contacts})

def DeleteCustomer(request, CusId):
    Cus = Contacts.objects.filter(id=CusId)
    Cus.delete()
    return redirect(CustomerContacts)

def AddCategory(request):
    return render(request, "AddCategory.html")

def SaveCategory(request):
    if request.method == "POST":
        C_Name = request.POST.get('CName')
        C_Image = request.FILES['CImg']
        C_Desc = request.POST.get('CDesc')
        obj = Category(CategoryName=C_Name, CategoryImage=C_Image, CategoryDesc=C_Desc)
        obj.save()
        messages.success(request, "Category Saved..!")
        return redirect(AddCategory)

def DisplayCategory(request):
    cat = Category.objects.all()
    return render(request, "DsiplayCategory.html", {'cat':cat})

def EditCategory(request, CatId):
    cat = Category.objects.get(id=CatId)
    return render(request, "EditCategory.html", {'cat':cat})

def UpdateCategory(request, Catid):
    if request.method == "POST":
        C_Name = request.POST.get('CName')
        C_Desc = request.POST.get('CDesc')
        try:
            C_Image = request.FILES['CImg']
            fs = FileSystemStorage()
            file = fs.save(C_Image.name, C_Image)
        except MultiValueDictKeyError:
            file=Category.objects.get(id=Catid).CategoryImage
        Category.objects.filter(id=Catid).update(CategoryName=C_Name, CategoryImage=file, CategoryDesc=C_Desc)
        messages.success(request, "Category Updated..!")
        return redirect(DisplayCategory)

def DeleteCategory(request, catid):
    caats = Category.objects.filter(id=catid)
    caats.delete()
    messages.success(request, "Category Deleted..!")
    return redirect(DisplayCategory)

def AddProduct(request):
    cat = Category.objects.all()
    return render(request, "AddProduct.html", {'cat':cat})

def SaveProduct(request):
    if request.method == "POST":
        P_Cat = request.POST.get('PCat')
        P_Name = request.POST.get('PName')
        P_Quant = request.POST.get('PQuant')
        P_Price = request.POST.get('PPrice')
        P_Desc = request.POST.get('PDesc')
        P_Origin = request.POST.get('POrigin')
        P_Manu = request.POST.get('PManu')
        P_Img1 = request.FILES['Pimg1']
        P_Img2 = request.FILES['Pimg2']
        P_Img3 = request.FILES['Pimg3']
        obj = Product(ProductCat=P_Cat, ProductName=P_Name, ProductQuantity=P_Quant,
                      ProductPrice=P_Price, ProductDesc=P_Desc, ProductOrigin=P_Origin,
                      ProductManu=P_Manu, ProductImage1=P_Img1, ProductImage2=P_Img2, ProductImage3=P_Img3)
        obj.save()
        messages.success(request, "Product Saved..!")
        return redirect(AddProduct)

def DisplayProduct(request):
    pro = Product.objects.all()
    return render(request, "DisplayProduct.html", {'pro':pro})

def EditProduct(request, ProId):
    pro = Product.objects.get(id=ProId)
    cat = Category.objects.all()
    return render(request, "EditProduct.html", {'pro':pro, 'cat':cat})

def UpdateProduct(request, Proid):
    if request.method == "POST":
        P_Cat = request.POST.get('PCat')
        P_Name = request.POST.get('PName')
        P_Quant = request.POST.get('PQuant')
        P_Price = request.POST.get('PPrice')
        P_Desc = request.POST.get('PDesc')
        P_Origin = request.POST.get('POrigin')
        P_Manu = request.POST.get('PManu')
        try:
            P_Img1 = request.FILES['Pimg1']
            fs = FileSystemStorage()
            file1 = fs.save(P_Img1.name, P_Img1)
        except MultiValueDictKeyError:
            file1 = Product.objects.get(id=Proid).ProductImage1
        try:
            P_Img2 = request.FILES['Pimg2']
            fs = FileSystemStorage()
            file2 = fs.save(P_Img2.name, P_Img2)
        except MultiValueDictKeyError:
            file2 = Product.objects.get(id=Proid).ProductImage2
        try:
            P_Img3 = request.FILES['Pimg3']
            fs = FileSystemStorage()
            file3 = fs.save(P_Img3.name, P_Img3)
        except MultiValueDictKeyError:
            file3 = Product.objects.get(id=Proid).ProductImage3
        Product.objects.filter(id=Proid).update(ProductCat=P_Cat, ProductName=P_Name, ProductQuantity=P_Quant,
                                ProductPrice=P_Price, ProductDesc=P_Desc, ProductOrigin=P_Origin,
                                ProductManu=P_Manu, ProductImage1=file1, ProductImage2=file2, ProductImage3=file3)
        messages.success(request, "Product Updated..!")
        return redirect(DisplayProduct)

def DeleteProduct(request, proid):
    pros = Product.objects.filter(id=proid)
    pros.delete()
    messages.success(request, "Product Deleted..!")
    return redirect(DisplayProduct)

def Login(request):
    return render(request, "admin_login.html")

def AdminLogin(request):
    if request.method == "POST":
        Username = request.POST.get('username')
        Password = request.POST.get('pass')
        if User.objects.filter(username__contains=Username).exists():
            user = authenticate(username=Username, password=Password)
            if user is not None:
                login(request, user)
                request.session['username'] = Username
                request.session['password'] = Password
                messages.success(request, "Welcome..!")
                return redirect(IndexPage)
            else:
                messages.error(request, "Incorrect Password..!")
                return redirect(Login)
        else:
            messages.warning(request, "Invalid Username..!")
            return redirect(Login)

def AdminLogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "You have been Logged out..!")
    return redirect(Login)