from . models import Expense,ExpenseCategory
from django import forms

class addExpenseCategoryForm(forms.ModelForm):
    """Form definition for addExpenseCategory."""
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        """Meta definition for addExpenseCategoryform."""

        model = ExpenseCategory
        fields = ('title',)


class addExpenseForm(forms.ModelForm):
    """Form definition for addExpense."""
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    amount=forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    # bill=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))


    class Meta:
        """Meta definition for addIncomeform."""

        model = Expense
        fields = '__all__'

    def __init__(self, user, *args, **kwargs):
        super(addExpenseForm, self).__init__(*args, **kwargs)
        self.fields['expense_category']=forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}),
                                                                                            queryset=ExpenseCategory.objects.filter(user=user))