from django.urls import path
from . import views
urlpatterns = [
    path('addIncomeCategory',views.addIncomeCategory,name='addIncomeCategory'),
    path('editIncomeCategory/<int:id>',views.editIncomeCategory,name='editIncomeCategory'),
    path('deleteIncomeCategory/<int:id>',views.deleteIncomeCategory,name='deleteIncomeCategory')
]