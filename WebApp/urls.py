from django.urls import path
from WebApp import views

urlpatterns = [
    path('SignupPage/', views.SignupPage, name="SignupPage"),
    path('SaveSignup/', views.SaveUser, name="SaveSignup"),
    path('', views.User_Login, name="UserLogin"),
    path('UserLogout/', views.User_Logout, name="UserLogout"),
    path('SigninPage/', views.SigninPage, name="SigninPage"),
    path('HomePage/', views.HomePage, name="HomePage"),
    path('ProductPage/', views.ProductPage, name="ProductPage"),
    path('CategoryPage/<CatName>/', views.CategoryPage, name="CategoryPage"),
    path('SingleProPage/<int:ProID>/', views.SingleProduct, name="SingleProPage"),
    path('AboutPage/', views.AboutPage, name="AboutPage"),
    path('ContactPage/', views.ContactPage, name="ContactPage"),
    path('SaveContact/', views.SaveContact, name="SaveContact"),
    path('SaveCart/', views.SaveCart, name="SaveCart"),
    path('ViewCart/', views.ViewCart, name="ViewCart"),
    path('DeleteCartItem/<int:item>/', views.DeleteCartItem, name="DeleteCartItem"),
    path('CheckoutPage/', views.CheckoutPage, name="CheckoutPage"),
    path('SaveOrder/', views.SaveOrder, name="SaveOrder"),
    path('PaymentPage/', views.PaymentPage, name="PaymentPage"),
]