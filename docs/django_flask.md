# Django vs Flask

## Introdução

No contexto de desenvolvimento Python para WEB, dois frameworks despontam como expoentes de mercado. São eles Django e Flask.

Assim, para o desenvolvimento das funcionalidades python a serem distribuídas enquanto serviço web no contexto da Nasajon, surge de imediato a questão sobre qual o framework mais adequado?

Para responder esta pergunta seguem algumas breves considerações levantadas após rápido esforço de pesquisa. Considerações estas que serão apresentadas em diferentes pontos de vista:

## Perspectivas

### Popularidade

|Framework      | Django | Flask |
|---------------|--------|-------|
|GitHub Stars   |45.4k   |47.6k  |
|GitHub Forks   |19.6k   |13.1k  |
|GitHub Whatches|2.2k    |2.3k   |

Como se pode notar, a comparação das métricas referentes aos repositórios de cada framework revelam que não há diferenças substanciais com relação a popularidade comparativa entre eles, antes ambos se revelam aplamente demandados no mercado.

### Funcionalidades e Características

|Framework                      |Django|Flask|
|-------------------------------|:----:|:---:|
|Controle de Rotas              |X     |X    |
|Template FrontEnd              |X     |X    |
|Servidor Dev Imbutido          |X     |X    |
|Debug                          |X     |X    |
|QuickStart via linha de comando|X     |     |
|Controle de conexão com o banco|X     |     |
|Solução ORM                    |X     |     |
|Solução de atualização MER     |X     |     |
|Arquitetura MVC                |X     |     |
|Browseable API                 |X     |     |
|Admin Interface                |X     |     |
|Arquitetura arbitrária         |      |X    |
|Rotas via anotation            |      |X    |
|Simplicidade                   |      |X    |
|Aprendizado Rápido             |      |X    |
|Leveza na execução             |      |X    |

Como se pode ver, o Django apresenta mais funcionalidades genéricas para uma aplicação web. Contudo isto se deve primordialmente as propostas de cada framework:

Enquanto o Django se propõe a ser uma framework completo para desenvolvimento de grandes aplicações web, o Flask procura se apresentar enquanto microframework, focado em simplicidade e minimalismo.

Mesmo assim, esta diferença não é imediatamente tido pela comunidade como um defeito do Flask. Antes é vista como uma característica proposital, que não impede o uso do Flask para aplicações mais complexas, exigindo porém o uso de soluções de terceiros (como o SQL Alchemy, enquanto camada ORM).

Portanto, se por um lado, o Django já se apresenta enquanto middleware ou framework mais completo, por outro lado o Flask se apresenta como uma solução mais leve e minimalista.

### Cases

|Django              |Flask          |
|--------------------|---------------|
|Bradcasting Service |Pinterest      |
|Mozilla             |**LinkedIn**   |
|**Instagram**       |Flask Community|
|The Washington Times|               |
|**BitBucket**       |               |
|Disqus              |               |
|Nextdoor            |               |

Neste ponto o DJango apresenta mais (e importantes) referências. Mesmo assim, o Flask continua apresentando resultados bastante relevantes, uma vez que contém cases como: "LinkedIn" e "Pinterest".

## Conclusão
Conforme se pôde verificar por meio desta breve análise, o Django é mais adequado para aplicações web complexas, enquanto o Flask apresenta menor tempo de aprendizado e mais leveza na execução, sendo então mais adequado para soluções pontuais. Portanto, sugere-se:

* Adoção do Django para soluções cujo escopo seja complexo ou com grande potencial de extensão (e que portanto corram maior risco de despadronização pela maior recorrência de manutenção).
* Adoção do Flask para soluções pontuais, com pouco esfoço alocado, e de escopo conhecidamente limitado (que dispense também o uso do banco de dados).

## Referências
* Repositório do Django no Github: https://github.com/django/django, acesso em 22/11/2019, 17:21
* Repositório do Flask no Github: https://github.com/pallets/flask, acesso em 22/11/2019, 17:21
* Comparativo Django, Flask: https://www.educba.com/django-vs-flask/, acesso em 22/11/2019, 17:21
* Comparativo Django, Flask: https://imasters.com.br/back-end/flask-x-django-como-escolher-o-framework-correto-para-seu-aplicativo-web, acesso em 22/11/2019, 17:32
* Comparativo Django, Flask: https://www.treinaweb.com.br/blog/django-ou-flask-eis-a-questao/, acesso em 22/11/2019, 17:37
