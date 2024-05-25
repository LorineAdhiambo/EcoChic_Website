from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('team/', views.team, name='team'),
    path('milestones/', views.milestones, name='milestones'),
    path('wardrobe/', views.wardrobe, name='wardrobe'),
    path('recommendations/<int:user_id>/', views.recommendations, name='recommendations'),
    path('trends/', views.trends, name='trends'),
    path('lookbooks/', views.lookbooks, name='lookbooks'),
]