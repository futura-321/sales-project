import django_filters
from django_filters import CharFilter
from django import forms

from .models import mobileproduct


class product_filter_form(django_filters.FilterSet):
    brand = CharFilter(label="" ,lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder':'search brand','class': 'form-control'}))

    seller_name = CharFilter(field_name='seller__name', lookup_expr='icontains', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'search by seller name'}))

    class Meta:
        model = mobileproduct
        fields = ['brand','seller_name']

