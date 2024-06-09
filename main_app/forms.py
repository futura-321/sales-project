from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.forms import DateInput

from main_app.models import login_view, customer, Seller, mobileproduct, Payment, Feedback


class login_view_form(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = login_view
        fields = ('username', 'password1', 'password2')


class seller_form(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ('__all__')
        exclude = ('user', 'status1')


class Customer_form(forms.ModelForm):
    class Meta:
        model = customer
        fields = ('__all__')
        exclude = ('user', 'status2')


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = login_view
        fields = ("username", "password1", "password2")


class CustomerRegister(forms.ModelForm):
    class Meta:
        model = customer
        fields = ("__all__")
        exclude = ('user', 'status1')


class sellerRegister(forms.ModelForm):
    class Meta:
        model = Seller
        fields = "__all__"
        exclude = ('user', 'status2')


class mobile_product_form(forms.ModelForm):
    class Meta:
        model = mobileproduct
        fields = ('__all__')
        exclude = ('seller',)


class DocumentForm(forms.ModelForm):
    class Meta:
        model = mobileproduct
        fields = ('__all__')



class DateInput(forms.DateInput):
    input_type = 'date'


class PaymentForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Payment
        fields = ('__all__')
        exclude=('buy',)
        # for single field in exclude comma(,) is needed


class customer_feedback_form(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('subject','feedback')


