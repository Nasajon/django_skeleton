from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic.base import View

import json

# O decorator abaixo desabilita uma segurança padrão do django. Ver: https://docs.djangoproject.com/pt-br/2.2/ref/csrf/
@method_decorator(csrf_exempt, name='dispatch')
class AbstractView(View):

    def post(self, request, *args, **kwargs):

        # Lendo o corpo da requisição como um json:
        entrada = json.loads(request.body.decode())

        # Montando o dicionário de saída:
        saida = self.rest_post(request, entrada)
        
        # Retornando a response contendo um json com o dicionário de saída:
        return HttpResponse(json.dumps(saida))
    
    def rest_post(self, request, entrada):
        return dict()