from django import forms

from .models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = ProductOrder
        fields = '__all__'
