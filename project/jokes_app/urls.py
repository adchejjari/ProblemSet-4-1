from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('highlight/', views.highlight, name='highlight'),
    path('entry/<int:id>', views.entry,name='entry')
]