from django.urls import path
from .views import ResourceAPIView, GetListView
from .models import *
from .serializers import *
urlpatterns = [
    path('pizza/<int:pk>', ResourceAPIView.as_view(
        model = Pizza,
        resource_serializer = PizzaSerializer
    )),
    path('pizza-size/<int:pk>', ResourceAPIView.as_view(
        model = PizzaSize,
        resource_serializer = PizzaSizeSerializer
    )),
    path('pizza-topping/<int:pk>', ResourceAPIView.as_view(
        model = PizzaTopping,
        resource_serializer = PizzaToppingSerializer
    )),
    path('pizza-list/<str:page>',GetListView.as_view(
        model = Pizza,
        resource_serializer = PizzaSerializer
    ))
]