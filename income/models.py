from django.db import models
from account.models import Account
# Create your models here.

class IncomeCategory(models.Model):
    title=models.CharField(max_length=100)
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    class Meta:
        db_table="incomecategory"

    def __str__(self):
        return self.title

class Income(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateField()
    amount=models.FloatField()
    expense_category=models.ForeignKey(IncomeCategory,on_delete=models.CASCADE)

    class Meta:
        db_table='income'

    def __str__(self):
        return self.title+': Rs'+str(self.amount)