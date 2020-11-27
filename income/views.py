from django.shortcuts import render,redirect
from . forms import AddIncomeCategory,AddIncome
from django.contrib import messages

# Create your views here.

from . models import IncomeCategory,Income
def addIncomeCategory(request):
    if request.method=='GET':
        form=AddIncomeCategory()
        return render(request,'pages/addIncomeCategoryForm.html',{"form":form})
    else:
        myform=AddIncomeCategory(request.POST)
        data=myform.save(commit=False)
        data.user=request.user
        data.save()
        messages.success(request,"Income Category Added Sucessfully")
        return redirect('account')


def editIncomeCategory(request,id):
    c=IncomeCategory.objects.get(id=id)
    form=AddIncomeCategory(request.POST or None,instance=c)
    if form.is_valid():
        form.save()
        messages.success(request,"Sucessfully edited")
        return redirect('account')
    return render(request,'pages/editIncomeCategoryForm.html',{'form':form})


def deleteIncomeCategory(request,id):
    c=IncomeCategory.objects.get(id=id)
    c.delete()
    messages.success(request,'sucessfully deleted')
    return redirect('account')


def addIncome(request):
    if request.method=='GET':
        form=AddIncome(request.user)
        context={'form':form}
        return render(request,'pages/addincome.html',context)
    else:
        form=AddIncome(request.user,request.POST)
        form.save()
        messages.success(request,"Sucessfully saved!")
        return redirect('account')

def editIncome(request,id):
    c=Income.objects.get(id=id)
    form=AddIncome(request.user,request.POST or None ,instance=c)
    if form.is_valid():
        form.save()
        messages.success(request,"Sucessfully edited")
        return redirect('account')
    context={'form':form}
    return render(request,'pages/editIncome.html',context)

def deleteIncome(request,id):
    c=Income.objects.get(id=id)
    c.delete()
    messages.success(request,"Sucessfully deleted")
    return redirect('account')