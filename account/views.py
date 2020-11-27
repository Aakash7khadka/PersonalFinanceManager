from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from . models import Account
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from income.models import IncomeCategory,Income
from expense.models import ExpenseCategory,Expense
# Create your views here.
def signin(request):
    if request.method=="GET":
        return render(request,'pages/login.html')
    else:
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('account')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('signin')
            



def register(request):
    if request.method=="GET":
        return render(request,'pages/register.html')
    else:
        email=request.POST['email']
        contact=request.POST['contact']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        if pass1 == pass2:
            a=Account(email=email,contact_no=contact)
            a.set_password(pass1)
            a.save()
            messages.success(request,"account created sucessfully")
            return redirect('signin')
        else:
            messages.error(request,"Passwords donot match")
            return redirect('signup')

        return HttpResponse(request.method)


# def profile(request):
#     if request.user.is_authenticated:

#         return render(request,'pages/profile.html')
#     else:
#         return redirect('signin')

@login_required(login_url='signin')
def profile(request):
    incomeCategory=IncomeCategory.objects.filter(user=request.user)[:5]
    income=Income.objects.filter(expense_category__in=incomeCategory)
    expenseCategory=ExpenseCategory.objects.filter(user=request.user)
    expense=Expense.objects.filter(expense_category__in=expenseCategory)
    return render(request,'pages/profile.html',{'incomeCategory':incomeCategory,'income':income,'expenseCategory':expenseCategory,'expense':expense})

def signout(request):
    logout(request)
    return redirect("signin")
