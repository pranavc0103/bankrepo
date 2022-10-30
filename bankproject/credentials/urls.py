from . import views
from django.urls import path

urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('newpage',views.newpage,name='newpage'),
    path('form',views.form,name='form'),
    path('messagepage',views.messagepage,name='messagepage'),
]