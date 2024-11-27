from django.urls import path
from AdminApp import views

urlpatterns = [
    path('Admin/', views.IndexPage, name="Admin"),

    path('CustomerContact/', views.CustomerContacts, name="CustomerContact"),
    path('DeleteCustomer/<int:CusId>/', views.DeleteCustomer, name="DeleteCustomer"),

    path('AddCategory/', views.AddCategory, name="AddCategory"),
    path('SaveCategory/', views.SaveCategory, name="SaveCategory"),
    path('ViewCategory/', views.DisplayCategory, name="ViewCategory"),
    path('EditCategory/<int:CatId>/', views.EditCategory, name="EditCategory"),
    path('UpdateCategory/<int:Catid>/', views.UpdateCategory, name="UpdateCategory"),
    path('DeleteCategory/<int:catid>/', views.DeleteCategory, name="DeleteCategory"),

    path('AddProduct/', views.AddProduct, name="AddProduct"),
    path('SaveProduct/', views.SaveProduct, name="SaveProduct"),
    path('ViewProduct/', views.DisplayProduct, name="ViewProduct"),
    path('EditProduct/<int:ProId>/', views.EditProduct, name="EditProduct"),
    path('UpdateProduct/<int:Proid>/', views.UpdateProduct, name="UpdateProduct"),
    path('DeleteProduct/<int:proid>/', views.DeleteProduct, name="DeleteProduct"),

    path('AdminLogin/', views.Login, name="AdminLogin"),
    path('AdminAuth/', views.AdminLogin, name="AdminAuth"),
    path('AdminLogout/', views.AdminLogout, name="AdminLogout")
]