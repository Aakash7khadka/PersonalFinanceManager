from . models import IncomeCategory
from django import forms


class AddIncomeCategory(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=IncomeCategory
        fields=['title',]
