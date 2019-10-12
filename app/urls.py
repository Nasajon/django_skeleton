from django.urls import path

from . import views

from app.view.ping import PingView

# TODO Adicionar aqui novos mapeamentos de URLs:
# Pode ver o exemplo PingPong
urlpatterns = [
    path('', views.index, name='index'),
    path('ping/', PingView.as_view(), name='ping'),
]