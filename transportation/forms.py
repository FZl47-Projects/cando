from django import forms
from . import models


class AddressCreateForm(forms.ModelForm):

    class Meta:
        model = models.Address
        exclude = ('map_address',)