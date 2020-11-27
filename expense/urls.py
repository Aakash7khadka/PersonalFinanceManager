from django.urls import path
from . import views
urlpatterns = [
    path('addExpenseCategory/',views.addExpenseCategory,name='addExpenseCategory'),
    path('deleteExpenseCategory/<int:id>/',views.deleteExpenseCategory,name='deleteExpenseCategory'),
    path('editExpenseCategory/<int:id>/',views.editExpenseCategory,name='editExpenseCategory'),
    path('addExpense/',views.addExpense,name='addExpense'),
    path('deleteExpense/<int:id>/',views.deleteExpense,name='deleteExpense'),
    path('editExpense/<int:id>/',views.editExpense,name='editExpense'),
]