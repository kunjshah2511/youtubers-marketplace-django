from django.urls import path

from . import views

urlpatterns=[
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('logout',views.logout_user,name="logout"),
    # Here we are using logout_user for views because there is an built-in function named logout so that name is unavailable
    path('dashboard',views.dashboard,name="dashboard"),
]
    