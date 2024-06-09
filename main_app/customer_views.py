from django.http import request
from django.shortcuts import render, redirect
from main_app.filters import product_filter_form
from main_app.forms import PaymentForm, customer_feedback_form
from main_app.models import mobileproduct, customer, Cart, Payment, Buy, Feedback


def customer_product_view(request):
    data = mobileproduct.objects.all()
    searched_form = product_filter_form(request.GET, queryset=data)
    # qs-->query set
    data = searched_form.qs
    context = {'data': data, 'searched_form': searched_form}
    return render(request, "customer/customer_product_view.html", context)


def add_to_cart(request, id):
    customer_object = customer.objects.get(user=request.user)
    product_object = mobileproduct.objects.get(id=id)
    print(customer_object)
    print(product_object)
    cart_obj = Cart(customer=customer_object, product=product_object)
    cart_obj.save()
    return redirect('customer_product_view')

def view_cart(request):
        customer_object = customer.objects.get(user=request.user)
        cart_objects = Cart.objects.filter(customer=customer_object)
        data = cart_objects
        return render(request, "customer/view_cart.html", {'data': data})

def delete_cart(request,id):
    data=Cart.objects.get(id=id)
    data.delete()
    return redirect("view_cart")


def buy(request, cart_id):
    if request.method == 'POST':
        cart_object = Cart.objects.get(id = cart_id)
        cart = cart_object
        print(cart)
        quantity =int(request.POST.get('quantity',0))
        print(quantity)
        adress = request.POST.get('adress')
        print(adress)
        phone = request.POST.get('phone')
        print(phone)
        price = int(cart_object.product.price)
        print(price)
        amount = quantity*price
        print(amount)
        buy_object = Buy(cart= cart ,phone = phone,adress = adress,quantity= quantity,amount = amount)
        buy_object.save()
        current_obect_id = buy_object.id
        return redirect("payment", buy_id = current_obect_id)
    return render(request, "customer/buy_now.html")




def payment(request, buy_id):
    data = PaymentForm()
    buy_object = Buy.objects.get(id = buy_id)
    if request.method == 'POST':
        data = PaymentForm(request.POST)
        if data.is_valid():
            pay_object = data.save(commit = False)
            pay_object.buy = buy_object
            pay_object.save()
            cart_object =buy_object.cart
            cart_object.status = 1
            cart_object.save()
            return redirect('view_cart')
    return render(request, 'customer/payment.html', {'data':data, 'buy_object':buy_object})

def my_orders(request):
     pay_objects = Payment.objects.filter(buy__cart__customer__user=request.user)
     return render(request, 'customer/view_my_orders.html', {'pay_objects': pay_objects})



def customer_feed_back(request):
    feedback_form_data = customer_feedback_form()
    if request.method == 'POST':
        feedback_form_data = customer_feedback_form(request.POST)
        if feedback_form_data.is_valid():
            feedback_object = feedback_form_data.save(commit = False)
            feedback_object.customer = customer.objects.get(user = request.user)
            feedback_object.save()
            return redirect('customer_dash')
    return render(request, "customer/customer_feed_back.html",{'feedback_form_data':feedback_form_data})



def customer_view_feedbacks(request):
    feedback_objects = Feedback.objects.filter(customer__user = request.user)
    return render(request, "customer/view_feedbacks.html",{'feedback_objects':feedback_objects })


# def feedback_reply(request):


