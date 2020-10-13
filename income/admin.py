from django.contrib import admin

# Register your models here.
from . models import IncomeCategory,Income

admin.site.register([Income,IncomeCategory])