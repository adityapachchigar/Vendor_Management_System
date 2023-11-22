from django import forms
from .models import VendorModel

class CreateVendorForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = VendorModel