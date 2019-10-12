# DJANGO SKELETON
Este repositório contém o esqueleto de uma aplicação básica de exemplo para o desenvolvimento de APIs Rest por meio do DJango (Python).

## Utilizando o Skeleton
1. Clone este repositório.
2. Copie o conteúdo do mesmo no repositório de destino.
3. Customize a aplicação criando os controles de rotas conforme desejado (explicado abaixo).
4. Copie o arquivo "common.env.dist" criando um "common.env".
5. Configure no arquivo "common.env" os parâmetros de comunicação com o banco de dados.
   1. A variável "database_driver" pode receber um dos seguintes valores: "postgres", "mysql" e "oracle".

## Customizando Rotas
Segue os passos para a criação de uma nova rota:
1. Edite o arquivo "app/urls.py".
2. Crie uma classe nova para controle da nova rota, estendo a classe "app.view.abstract_view.AbstractView".
3. Sobreescreva o método "rest_post()", adicionando o comportamento de controle de sua rota:
   1. Este método recebe uma "entrada" do tipo dict, correspondente ao json recebido no corpo de uma requisição post, e pressupõe que se retorne um dict de resultado, o qual será codificado no formato json, e adicionado no corpo da resposta HTTP.
   2. Obs.: Pode-se usar a classe "app.view.ping.PingView" como exemplo.
4. Adicione um novo padrão de url apontando para a view recém criada, no arquivo "app.urls.py":
   1. Obs.: Pode-se usar a rota do "PingView" como exemplo.

## Testando a Aplicação
1. Inicie o banco de dados de exemplo (se desejar):
```shell
docker-compose up postgres
```
2. Instale as dependências do projeto:
```shell
sudo python3 -m pip install -r requirements.txt
```
3. Inicie o servidor de aplicação de desenvolvimento:
```shell
python3 manage.py runserver
```
4. Abra a URL: http://localhost:8000 (adicione a rota que desejar, porém há um template de exemplo sendo renderizado no index da aplicação).