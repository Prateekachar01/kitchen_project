from django.urls import path
from .views import UserRegView,UserLoginView,UserById,DeleteUser

urlpatterns=[
    path("register/",UserRegView.as_view(),name='register'),
    path("login/",UserLoginView.as_view(),name='login'),
    path("details/<str:userId>/",UserById.as_view(),name='details'),
    path("delete/<str:userId>/",DeleteUser.as_view(),name='delete'),
]
