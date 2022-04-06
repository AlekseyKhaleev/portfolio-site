from django.urls import path
from . import views


app_name = 'portfolio'

urlpatterns = [
    path('', views.all_cards, name='all_cards'),
    path('<int:card_id>/', views.detail, name='detail'),
    ]

