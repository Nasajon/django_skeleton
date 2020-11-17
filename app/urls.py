from django.urls import path

from . import views

from app.view.ping import PingView
from app.view.salario_liquido import SalarioLiquidoView

# TODO Adicionar aqui novos mapeamentos de URLs:
# Pode ver o exemplo PingPong
urlpatterns = [
    path('', views.index, name='index'),
    path('ping/', PingView.as_view(), name='ping'),
    path('salario_liquido_model/', SalarioLiquidoView.as_view(),
         name='salario_liquido_model'),
    path('ping2/', views.ping2, name='ping2'),
]
