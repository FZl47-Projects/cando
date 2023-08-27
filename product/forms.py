from django import forms
from . import models


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'


class FactorCakeImageForm(forms.ModelForm):
    description = forms.CharField(max_length=400, required=False)

    class Meta:
        model = models.FactorCakeImage
        fields = '__all__'
