from django.db import models
from account.models import Account
# Create your models here.

class ExpenseCategory(models.Model):
    title=models.CharField(max_length=100)
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    class Meta:
        db_table="expensecategory"

    def __str__(self):
        return self.title

class Expense(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateField()
    amount=models.FloatField()
    bill=models.ImageField(upload_to='bill/')
    expense_category=models.ForeignKey(ExpenseCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.title+': Rs'+str(self.amount)
