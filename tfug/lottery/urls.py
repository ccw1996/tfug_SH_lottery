from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path(r'update/',views.update,name="update"),
    path(r'get/',views.get,name="get"),
    path(r'allpeople/',views.allpeople,name="allpeople"),
    path(r'luckypeople/',views.luckypeople,name="luckypeople"),
]
