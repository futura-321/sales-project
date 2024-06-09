from django.shortcuts import render, redirect

from main_app.filters import product_filter_form
from main_app.forms import CustomerRegister, sellerRegister
from main_app.models import customer, Seller, mobileproduct, Feedback, Payment


def customer_details(request):
    customers=customer.objects.all()
    print(customers)
    print("hlo")
    return render(request,"admin/customer_details.html",{'customers':customers})

def seller_details(request):
    sellers=seller.objects.all()
    return render(request, "admin/seller_details.html",{'sellers':sellers})

def customer_update(request,id):
    obj=customer.objects.get(pk=id)
    customer_form=CustomerRegister(instance=obj)
    if request.method=="POST":
        customer_form=CustomerRegister(request.POST,instance=obj)
        if customer_form.is_valid():
            customer_form.save()
            return redirect("customer_details")
    return render(request,"admin/customer_update.html",{'customer_form':customer_form})

def customer_delete(request,id):
    data=customer.objects.get(id=id)
    data.delete()
    return redirect("customer_details")

def seller_update(request,id):
    obj=seller.objects.get(id=id)
    seller_form=sellerRegister(instance=obj)
    if request.method=="POST":
        seller_form=CustomerRegister(request.POST,instance=obj)
        if seller_form.is_valid():
            seller_form.save()
            return redirect("seller_details")
    return render(request,"admin/product_update.html",{'seller_form':seller_form})


def seller_delete(request,id):
    data=seller.objects.get(id=id)
    data.delete()
    return redirect("seller_details")

def admin_product_view(request):
    data = mobileproduct.objects.all()
    searched_form = product_filter_form(request.GET, queryset=data)
    # qs-->query set
    data = searched_form.qs
    context = {'data': data, 'searched_form': searched_form}
    return render(request,"admin/admin_product_views.html",context)


def admin_view_feedbacks(request):
    feedback_objects = Feedback.objects.all()
    return render(request, "admin/customers_feedback.html",{'feedback_objects':feedback_objects})


def admin_view_orders(request):
    pay_objects = Payment.objects.all()
    pay_filter_form_data = pay_filter_form(request.GET, queryset=pay_objects)
    pay_objects = pay_filter_form_data.qs
    context = {'pay_objects':pay_objects, 'pay_filter_form_data':pay_filter_form_data}
    return render(request, "admin/admin_view_orders.html", context)