from django.urls import path
from .views import HomeMakerRegView,HomeMakerLoginView,HomeMakerApproveView,NearyByMakers

urlpatterns=[
    path("register/",HomeMakerRegView.as_view(),name='register'),
    path("login/",HomeMakerLoginView.as_view(),name='login'),
    path("approve/<str:userId>/",HomeMakerApproveView.as_view()),
    path("nearby/<area>/",NearyByMakers.as_view(),name='nearby'),
]