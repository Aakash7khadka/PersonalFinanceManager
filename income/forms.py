from . models import IncomeCategory,Income
from django import forms


class AddIncomeCategory(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=IncomeCategory
        fields=['title',]


class AddIncome(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    amount=forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control'}))

    
    class Meta:
        model=Income
        fields='__all__'

    def __init__(self, user, *args, **kwargs):
        super(AddIncome, self).__init__(*args, **kwargs)
        self.fields['expense_category']=forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}),
                                                                                            queryset=IncomeCategory.objects.filter(user=user))