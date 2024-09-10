from django.urls import path
from .views import AddFoodView,FoodDetailsById

urlpatterns=[
    path("add/",AddFoodView.as_view(),name='add'),
    path("details/<userId>/",FoodDetailsById.as_view(),name='details'),
]