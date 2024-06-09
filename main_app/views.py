from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from main_app.forms import Customer_form, CustomerRegister, login_view_form, seller_form, LoginRegister
from main_app.models import Seller, customer


# Create your views here.
def main (request):
    return render(request,"home.html")
def dash(request):
    return render(request,"dash.html")

def Login(request):
    if request.method=='POST':
        username = request.POST.get('user')
        password= request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect("admin_dash")
            elif user.is_seller:
                return redirect("seller_dash")
            elif user.is_customer:
                return redirect("customer_dash")


    return render(request,"login.html")

@login_required(login_url='login')
def customer_register(request):
    form1=login_view_form()
    form2=Customer_form()
    if request.method=="POST":
        form1=login_view_form(request.POST)
        form2=Customer_form(request.POST)
        if form1.is_valid() and form2.is_valid():
            a=form1.save(commit=False)
            a.is_customer=True
            a.save()
            user1=form2.save(commit=False)
            user1.user=a
            user1.save()
            return redirect("/")

    return render(request,"customer/customer_register.html",{'form1':form1,'form2':form2})
@login_required(login_url='login')
def seller_register(request):
        form1 = login_view_form()
        form2 = seller_form()
        if request.method == "POST":
            form1 = login_view_form(request.POST)
            form2 = seller_form(request.POST)
            if form1.is_valid() and form2.is_valid():
                a = form1.save(commit=False)
                a.is_seller = True
                a.save()
                user1 = form2.save(commit=False)
                user1.user = a
                user1.save()
                return redirect("/")

        return render(request, "seller_register.html", {'form1': form1, 'form2': form2})




def admin_dash(request):
    return render(request,"admin/admin_dash.html")

def customer_dash(request):
    return render(request,"customer/customer_dash.html")
@login_required(login_url='login')
def seller_dash(request):
    return render(request,"seller/seller_dash.html")

@login_required(login_url='login')
def customer_details(request):
    return render(request,"admin/customer_details.html")

@login_required(login_url='login')
def seller_details(request):
    return render(request,"admin/seller_details.html")
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect("Login")