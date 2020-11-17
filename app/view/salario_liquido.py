from django.http import HttpResponse
from app.view.abstract_view import AbstractView

import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
import tensorflow as tf
import random as python_random
import urllib.request
import uuid

from typing import Any, Dict, List, Tuple


class SalarioLiquidoView(AbstractView):

    PATH_STATS_NORM = 'file:////home/sergiosilva/@work/django_skeleton/models/norm_valor_salario_liquido_sem_rubricas_32.csv'
    PATH_MODEL = 'file:////home/sergiosilva/@work/django_skeleton/models/valida_salario_liquido_32.h5'
    PATH_STATS_ERRORS = 'file:////home/sergiosilva/@work/django_skeleton/models/erros_percentuais_salario_liquido_32.csv'

    def rest_post(self, request, entrada):

        # Transformando a entrada num Pandas DataFrame
        ds = pd.DataFrame(entrada)

        # Semeando os números aleatórios
        seed = 0
        np.random.seed(seed)
        python_random.seed(seed)
        tf.random.set_seed(seed)

        # Separando os dados de intresse
        cols = [
            'empresa_codigo', 'departamento', 'matricula',
            'salario_fixo', 'anos_trabalhados', 'numerohorasmensais',
            'dias_afastamento', 'dias_falta', 'dependentes_ir', 'horas_extras',
            'atraso',
            'dias_acidente_trabalho', 'dependentes_salario_familia',
            'pedido_vale_transporte', 'valor_emprestimo', 'percentual_pensao',
            'R_1099',
            'R_1201', 'R_1207', 'R_1211', 'R_1299', 'R_1604', 'R_1619', 'R_1650',
            'D_1352', 'D_9219', 'D_9254',
            'salario_liquido'
        ]
        x = ds[cols]

        # Separando as colunas de identificação do funcionário
        empresa = x.pop('empresa_codigo')
        departamento = x.pop('departamento')
        matricula = x.pop('matricula')

        # Copiando os valores da variável dependente
        y = x['salario_liquido'].copy()

        # Recuperando as estatísticas da base de treino
        stats = pd.read_csv(
            SalarioLiquidoView.PATH_STATS_NORM, header=0, index_col=0)
        stats.set_index(stats.columns[0])

        # Normalizando os dados
        normed_x = self.norm(x, stats)

        # Retirando a variável dependente
        _ = normed_x.pop('salario_liquido')

        # Carregando o modelo
        model_path = self.download(SalarioLiquidoView.PATH_MODEL)
        model = load_model(model_path)

        # Prevendo os salários líquidos pelo modelo
        predict_normed_y = model.predict(normed_x).flatten()

        # Avaliando os erros
        predict_y = predict_normed_y * stats['std']['salario_liquido']
        erros = predict_y - y
        erros_abs = erros.abs()
        erros_percentuais = erros_abs / y * 100

        # Lendo as estatísitcas dos erros percentuais na validação
        stats_erro_percentual = pd.read_csv(
            SalarioLiquidoView.PATH_STATS_ERRORS, header=None, index_col=0)
        stats_erro_percentual = stats_erro_percentual.transpose()

        # Montando um dataframe de resultados
        dados = empresa.to_frame()
        dados['departamento'] = departamento
        dados['matricula'] = matricula
        dados['salario_liquido'] = y
        dados['salario_liquido_previsto'] = predict_y
        dados['erro'] = erros
        dados['erro_absoluto'] = erros_abs
        dados['erro_percentual'] = erros_percentuais

        # Filtrando os erros em alerta
        suspeitos = dados[dados.erro_percentual >=
                          stats_erro_percentual['mean'][1]]

        outros = dados[dados.erro_percentual <
                       stats_erro_percentual['mean'][1]]

        alerta = suspeitos[suspeitos.erro_percentual >= (
            stats_erro_percentual['mean'][1] + stats_erro_percentual['std'][1])]

        atencao = suspeitos[suspeitos.erro_percentual < (
            stats_erro_percentual['mean'][1] + stats_erro_percentual['std'][1])]

        # Ordenando o resultado (do maior erro percentual para o menor)
        alerta = alerta.sort_values(
            by='erro_percentual', ascending=False)

        atencao = atencao.sort_values(
            by='erro_percentual', ascending=False)

        outros = atencao.sort_values(
            by='erro_percentual', ascending=False)

        # Transformando os DataFrames em listas de dicionários
        colunas, alerta = self.dataframe_to_listdicts(alerta)
        colunas, atencao = self.dataframe_to_listdicts(atencao)
        colunas, outros = self.dataframe_to_listdicts(outros)

        # Montando o dicionário de saída:
        saida = dict()
        saida['columns'] = colunas
        saida['alerts'] = alerta
        saida['warnings'] = atencao
        saida['others'] = outros

        # Retornando a response em formato de dict:
        return saida

    def dataframe_to_listdicts(self, dataframe) -> Tuple[List[str], List[Dict[str, Any]]]:

        colunas = [col for col in dataframe.columns]

        dados = list()
        for _, row in dataframe.iterrows():
            linha = dict()

            for col in colunas:
                dado = row[col]

                linha[col] = dado

            dados.append(linha)

        return (colunas, dados)

    def norm(self, x, stats):
        return (x - stats['mean'] + stats['std']) / stats['std']

    def download(self, url: str) -> str:
        # Download to buffer
        response = urllib.request.urlopen(url, timeout=15)
        data = response.read()

        # Resolving path
        path = 'models/{}.h5'.format(str(uuid.uuid4()))

        # Writting buffer to disk
        with open(path, 'wb') as f:
            f.write(data)

        return path
