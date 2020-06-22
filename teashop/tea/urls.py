from django.urls import path
from .views import BaseView,AddItem,DeleteView
from django.conf.urls.static import static
from teashop import settings


urlpatterns =[
    path('',BaseView, name = "addview"),
    path('add/', AddItem, name ="additem"),
    path('delete/<int:id>/',DeleteView,name="deleteview"),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)