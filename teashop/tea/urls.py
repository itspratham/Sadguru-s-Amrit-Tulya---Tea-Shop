from django.urls import path
from .views import BaseView
urlpatterns =[
    path('',BaseView, name = "addview"),
    path('add/',)
    ]