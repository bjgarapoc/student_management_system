from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.student_table, name='index'),
    path('add/', views.home, name='add'),
    path('delete/<int:id>/',views.delete,name="delete")
]