from django.http import HttpResponse
from app.view.abstract_view import AbstractView

class PingView(AbstractView):

    def get(self, request, *args, **kwargs):
        
        # Procurando o parâmetro "ping" na requisição GET:
        if not ('ping' in request.GET):
            # Se não achar, ensina como usar:
            return HttpResponse('Para melhorar o teste passe um parâmetro "ping" na requisição.')
        
        # Retorna uma resposta ecoando o ping
        return HttpResponse('PONG! Você passou "{}"'.format(request.GET['ping']))

    def rest_post(self, request, entrada):

        # Montando o dicionário de saída:
        saida = dict()
        if not ('ping' in entrada):
            saida["msg"] = 'Para melhorar o teste passe um parâmetro "ping" num json no corpo da requisição.'
        else:
            saida["msg"] = 'PONG! Você passou "{}"'.format(entrada['ping'])
        
        # Retornando a response em formato de dict:
        return saida