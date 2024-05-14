from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_table, name='index'),
    path('add/', views.home, name='add'),
    path('add/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
