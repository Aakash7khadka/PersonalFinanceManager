from django.shortcuts import render,redirect
from . forms import addExpenseCategoryForm,addExpenseForm
from django.contrib import messages
# Create your views here.
from . models import Expense,ExpenseCategory

def addExpenseCategory(request):
    if request.method=="GET":
        form=addExpenseCategoryForm()
        context={'form':form}
        return render(request,'pages/addExpenseCategory.html',context)
    
    form=addExpenseCategoryForm(request.POST)
    data=form.save(commit=False)
    data.user=request.user
    data.save()
    messages.success(request,"Sucessfully added!")
    return redirect('account')

    
def deleteExpenseCategory(request,id):
    c=ExpenseCategory.objects.get(id=id)
    c.delete()
    messages.success(request,"Sucessfully deleted")
    return redirect("account")

def editExpenseCategory(request,id):
    c=ExpenseCategory.objects.get(id=id)
    form=addExpenseCategoryForm(request.POST or None,instance=c)
    if form.is_valid():
        form.save()
        messages.success(request,"Sucessfully edited")
        return redirect("account")
    return render(request,'pages/addExpenseCategory.html',{'form':form})


def addExpense(request):
    if request.method=='GET':
        form=addExpenseForm(request.user)
        context={'form':form}
        return render(request,'pages/addExpense.html',context)
    else:
        form=addExpenseForm(request.user,request.POST)
        form.save()
        messages.success(request,"Sucessfully saved!")
        return redirect('account')

def editExpense(request,id):
    c=Expense.objects.get(id=id)
    form=addExpenseForm(request.user,request.POST or None,instance=c)
    if form.is_valid():
        form.save()
        messages.success(request,"sucessfully edited")
        return redirect('account')
    
    return render(request,'pages/addExpense.html',{'form':form})

def deleteExpense(request,id):
    c=Expense.objects.get(id=id)
    c.delete()
    messages.success(request,"Sucessfully deleted")
    return redirect("account")
