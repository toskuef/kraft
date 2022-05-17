from django import forms

from dynamic_forms import DynamicField, DynamicFormMixin

from .models import Category, Group, Nomenclature


class NomenclatureForm(DynamicFormMixin, forms.ModelForm):

    def group_choices(form):
        category = form['category'].value()
        return Group.objects.filter(category=category)

    def initial_group(form):
        category = form['category'].value()
        return Group.objects.filter(category=category).first()

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        initial=Category.objects.first()
    )
    group = DynamicField(
        forms.ModelChoiceField,
        queryset=group_choices,
        initial=initial_group,
    )

    class Meta:
        model = Nomenclature
        fields = '__all__'
