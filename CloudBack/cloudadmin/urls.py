from django.urls import path
from .views import CloudAdminLoginView


urlpatterns=[
    path("login/",CloudAdminLoginView.as_view(),name='login'),
]
