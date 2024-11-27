import razorpay
from django.shortcuts import render, redirect
from AdminApp.models import Product, Category
from WebApp.models import Contacts, Signup,  Cart, Order
from django.contrib import messages


# Create your views here.
def SignupPage(request):
    return render(request, "Signup.html")

def SigninPage(request):
    return render(request, "Signin.html")

def HomePage(request):
    cat = Category.objects.all()
    car = Cart.objects.filter(UName=request.session['UName'])
    count = car.count()
    return render(request, "Home.html", {'cat':cat, 'count':count})

def ProductPage(request):
    products = Product.objects.all()
    car = Cart.objects.filter(UName=request.session['UName'])
    count = car.count()
    return render(request, "Product.html", {'products':products, 'count':count})

def CategoryPage(request, CatName):
    data = Product.objects.filter(ProductCat=CatName)
    car = Cart.objects.filter(UName=request.session['UName'])
    count = car.count()
    return render(request, "Category.html", {'data':data, 'count':count})

def SingleProduct(request, ProID):
    data = Product.objects.get(id=ProID)
    car = Cart.objects.filter(UName=request.session['UName'])
    count = car.count()
    return render(request, "SingleProduct.html", {'data':data, 'count':count})

def AboutPage(request):
    car = Cart.objects.filter(UName=request.session['UName'])
    count = car.count()
    return render(request, "About.html", {'count':count})

def ContactPage(request):
    car = Cart.objects.filter(UName=request.session['UName'])
    count = car.count()
    return render(request, "Contact.html", {'count':count})

def SaveContact(request):
    if request.method == "POST":
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Contact = request.POST.get('contact')
        Comment = request.POST.get('comment')
        obj = Contacts(Name=Name, Email=Email, Contact=Contact, Comment=Comment)
        obj.save()
        return redirect(ContactPage)

def SaveCart(request):
    if request.method == "POST":
        User = request.POST.get('user')
        product = request.POST.get('product')
        PPrice = request.POST.get('price')
        Quantity = request.POST.get('quantity')
        TotalPrice = request.POST.get('totalprice')
        try:
            PImg = Product.objects.get(ProductName=product)
            img = PImg.ProductImage1
        except Product.DoesNotExist:
            img = None
        obj = Cart(PQuantity=Quantity, PPrice=PPrice, PName=product,
                   Total=TotalPrice, UName=User, Image=img)
        obj.save()
        return redirect(ProductPage)

def ViewCart(request):
    car = Cart.objects.filter(UName=request.session['UName'])
    count = car.count()
    subtotal = 0
    delivery = 0
    total = 0
    for i in car:
        subtotal += i.Total
        if subtotal >= 100000:
            delivery = 9999
        else:
            delivery = 4999
        total = subtotal + delivery

    return render(request, "CartPage.html", {'car':car, 'subtotal':subtotal, 'delivery':delivery, 'total':total, 'count':count})

def DeleteCartItem(request, item):
    data = Cart.objects.filter(id=item)
    data.delete()
    return redirect(ViewCart)

def CheckoutPage(request):
    car = Cart.objects.filter(UName=request.session['UName'])
    count = car.count()
    subtotal = 000000000000
    delivery = 0
    total = 0
    for i in car:
        subtotal += i.Total
        if subtotal >= 100000:
            delivery = 9999
        else:
            delivery = 4999
        total = subtotal + delivery
    return render(request, "CheckoutPage.html", {'car':car, 'subtotal':subtotal, 'delivery':delivery, 'total':total, 'count':count})

def SaveOrder(request):
    if request.method == "POST":
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        Cntry = request.POST.get('country')
        Pin = request.POST.get('pincode')
        Addr = request.POST.get('addr')
        Town = request.POST.get('town')
        Cmnt = request.POST.get('comment')
        Total = request.POST.get('total')
        obj = Order(UName=Name, UMail=Email, Addr=Addr, Town=Town,
                     Contact=Phone, Comment=Cmnt, TotalPrice=Total, Country=Cntry, Pincode=Pin)
        obj.save()
        return redirect(PaymentPage)

def PaymentPage(request):
    customer = Order.objects.order_by('-id').first()  #To retrieve data from the last:means last data added/ last order placed is to be selected
    payy = customer.TotalPrice #Retrieve total price from order db
    amount = int(payy*100) #Converting ruppes to paisa
    payy_str = str(amount) #converting the amount to string for displaying purposes
    if request.method == "POST":
        order_currency = "INR"
        client = razorpay.Client(auth=('rzp_test_OUDYhMU2QeUU0h', 'txBLX6YSnR5SqPsZvuiIwznD'))
        payment = client.order.create({'amount':amount, 'currency':order_currency})
    return render(request, "PaymentPage.html", {'customer':customer, 'pay_str':payy_str})

def SaveUser(request):
    if request.method == "POST":
        Name = request.POST.get('username')
        Contact = request.POST.get('contact')
        Email = request.POST.get('email')
        Pass = request.POST.get('password')
        RPass = request.POST.get('repeatpassowrd')
        obj = Signup(UName=Name, UContact=Contact, UEmail=Email, UPass=Pass, URPass=RPass)
        if Signup.objects.filter(UName=Name).exists():
            messages.warning(request,"User Already Exists..!")
            return redirect(SignupPage)
        elif Signup.objects.filter(UEmail=Email).exists():
            messages.error(request, "EMail Already Exists..!")
            return redirect(SignupPage)
        obj.save()
        messages.success(request, "Sign In Successful..!")
        return redirect(SigninPage)

def User_Login(request):
    if request.method == "POST":
        un = request.POST.get('Username')
        pswrd = request.POST.get('Password')
        if Signup.objects.filter(UName=un, UPass=pswrd).exists():
            request.session['UName'] = un
            request.session['UPass'] = pswrd
            messages.success(request, "Welcome..!")
            return redirect(HomePage)
        else:
            messages.error(request, "Incorrect Password..!")
            return redirect(SigninPage)
    else:
        messages.warning(request, "Invalid Username..!")
        return redirect(SigninPage)


def User_Logout(request):
    del request.session['UName']
    del request.session['UPass']
    messages.success(request, "You Have Logged Out..!")
    return redirect(SigninPage)
