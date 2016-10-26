from django import forms
from address.forms import AddressField


class AddressForm(forms.Form):
    address = AddressField()
    AdditionalAddress = forms.CharField(max_length=255)