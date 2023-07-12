from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('delete/<str:id>/',views.delete,name='delete'),
    path('deleteall/',views.deleteall,name='deleteall'),
    path('sortbyrollno',views.sortbyrollno,name='sortbyrollno')
]
