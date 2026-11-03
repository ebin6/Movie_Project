from django.urls import path

from accounts import views

urlpatterns=[
    path("register/",views.signUp,name="register"),
    path("login/",views.signIn,name="login"),
    path("logout/",views.Logout,name="logout")
]