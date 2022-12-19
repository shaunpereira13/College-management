from django.urls import path
from .import views

urlpatterns=[
    path('',views.home, name='home'),
    path('login/<str:pk>/',views.loginstudent, name="login"),
    path('loginteach/',views.loginteacher, name="loginteach"),
]
