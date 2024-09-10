from django.urls import path
from .views import AddAreaView

urlpatterns=[
    path("add/",AddAreaView.as_view(),name='add'),
]