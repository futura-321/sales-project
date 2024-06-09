
from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.
class login_view(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

class customer(models.Model):
    user=models.ForeignKey(login_view,on_delete=models.CASCADE,related_name='customer')
    name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
       return self.name

    def is_valid(self):
        pass


class Seller(models.Model):
    user = models.ForeignKey(login_view, on_delete=models.CASCADE, related_name='seller')
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def is_valid(self):
        pass


class mobileproduct(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='mobileproducts')
    model_number=models.CharField(max_length=250)
    model_name=models.CharField(max_length=250)
    sim_type=models.CharField(max_length=250)
    color=models.CharField(max_length=250)
    brand=models.CharField(max_length=250)
    price=models.CharField(max_length=250)
    image = models.FileField(upload_to='documents/')



class Cart(models.Model):
    product = models.ForeignKey(mobileproduct, on_delete=models.CASCADE, related_name='cart_customer')
    customer = models.ForeignKey(customer, on_delete=models.CASCADE, related_name='cart_product')
    status = models.IntegerField(default=0)




class Buy(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    adress = models.TextField()
    quantity=models.CharField(max_length=20)
    amount=models.CharField(max_length=100)




class Payment(models.Model):
    buy = models.ForeignKey(Buy, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    date = models.DateField()


class Feedback(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE, related_name = "feedback_customer")
    date = models.DateField(auto_now = True)
    subject = models.CharField(max_length = 250)
    feedback = models.TextField()
    reply = models.TextField(blank = True, null = True)




