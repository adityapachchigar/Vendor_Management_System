from django import forms
from .models import VendorModel

class CreateVendorForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = VendorModel
        
class AllThree(forms.Form):
    vendor_code = forms.CharField(max_length=50)