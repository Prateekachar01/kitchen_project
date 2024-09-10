from django.urls import path
from .views import AddOrderView ,OrderDetailsById,OrderDetailsByKitchenId,OrderDeliver


urlpatterns=[
    path("add/",AddOrderView.as_view(),name='add'),
    path('details/<userId>/',OrderDetailsById.as_view(),name='details'),
    path('kitchen/<kitchenId>/',OrderDetailsByKitchenId.as_view(),name='kitchen'),
    path('deliver/<kitchenId>/<id>/',OrderDeliver.as_view(),name='deliver'),
]
