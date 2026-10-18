from django import forms
from .models import ChaiVariety, ChaiReviews, Store, ChaiCertificate

class ChaiVarietyForm(forms.Form):
    chai_variety = forms.ModelChoiceField(queryset=ChaiVariety.objects.all(), label='Select a Chai Variety')
    