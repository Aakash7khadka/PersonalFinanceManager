from django.urls import path
from . import views
urlpatterns = [
    path('login',views.signin,name='signin'),
    path('register',views.register,name='signup'),
    path('',views.profile,name='account'),
    path('signout/',views.signout,name='signout')
]