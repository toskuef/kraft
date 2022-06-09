from django import forms
from django.core.exceptions import ValidationError

from .models import *
from .validation import validation_ru_letters, validation_phone




class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'

    def clean_last_name(self):
        return validation_ru_letters(self.cleaned_data['last_name'])

    def clean_first_name(self):
        return validation_ru_letters(self.cleaned_data['first_name'])

    def clean_family_name(self):
        return validation_ru_letters(self.cleaned_data['family_name'])

    def clean_phone(self):
        return validation_phone(self.cleaned_data['phone'])



class OrderForm(forms.ModelForm):
    """Создание заказа на первой итерации"""
    class Meta:
        model = Order
        fields = ['title']


class CommentForm(forms.ModelForm):
    text = forms.CharField()

    class Meta:
        model = Comment
        fields = ['text']


class TaskForm(forms.ModelForm):
    task = forms.CharField()
    executor = forms.ModelChoiceField(User.objects.all(), empty_label='Исполнитель')
    type_task = forms.ModelChoiceField(TypeTask.objects.all(), empty_label='Тип задачи')

    class Meta:
        model = Task
        fields = ['task', 'executor', 'deadline', 'type_task']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title']


class MeasuringForm(forms.ModelForm):
    class Meta:
        model = Measuring
        fields = ['measuring']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project']


