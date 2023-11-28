# Plantae: Biodiversidade Vegetal para as Gerações Futuras

Nosso projeto é baseado na ODS de número 2 "Fome zero e agricultura sustentável". Dentre os diversos micro objetivos desta ODS está presente o seguinte:

```
2.5 Até 2020, manter a diversidade genética de sementes, plantas cultivadas, animais de criação e domesticados e suas respectivas espécies selvagens,
inclusive por meio de bancos de sementes e plantas diversificados e bem geridos em nível nacional, regional e internacional,
e garantir o acesso e a repartição justa e equitativa dos benefícios decorrentes da utilização dos recursos genéticos e conhecimentos tradicionais associados,
como acordado internacionalmente.
```

A partir dele, desenvolvemos uma plataforma web onde o produtor agrícola consegue consultar quais as melhores plantas a serem cultivadas em determinada região baseada em clima, solo, e condições adversas. Para isso estamos utilizando API's disponibilizadas pela [Embrapa](https://www.agroapi.cnptia.embrapa.br/portal/) de forma aberta e freemium onde as consultas realizadas serão retornadas em forma de tabelas e descrição, a fim de colaborar com a disseminação de informações sobre a diversidade de plantas.

## Integrantes do Projeto

<b>Matheus Matias</b> <br>
`Github` [matheusoms](https://github.com/matheusoms)

<b>Pedro Penteado</b> <br>
`Github` [Dreppo](https://github.com/Dreppo)

<b>Pedro Otavio</b> <br>
`Github` [pedr0tavi0](https://github.com/pedr0tavi0)

## Desenvolvimento do projeto

`Desenvolvimento WEB:` Estamos utilizando para o desenvolvimento WEB as seguintes linguagens:
- Django
- JavaScript
- HTML5 e CSS3

`Desenvolvimento Backend:` Estamos utilizando para o desenvolvimento backend as seguintes linguagens:
- Python

`Banco de Dados:` Estamos utilizando para o desenvolvimento do banco de dados NoSQL as seguintes linguagens:
- MongoDB

## Requisitos para o Projeto

Banco de Dados [Mongo Database](https://www.mongodb.com/):
- Mongo Server
- Mongo Compass
- Porta localhost `27017`
Caso esteja no Linux deve-se usar o comando no CMD `sudo systemctl start mongod` para iniciar o server e
`sudo systemctl stop mongod` para parar o server
- Criar um Banco chamado PROJETO e uma coleção chamada semente
  
  
Backend [Python](https://www.python.org/):
- Python
- Ativar a Venv 
`virtualenv "nome do hambiente"`
`pip install -r requirements.txt`
No Windows `cd venv` `cd scripts` `activate.bat`
No Linux `source venv/bin/activate`
- Rodar o servidor
`cd Plantae/`
`python manage.py runserver`
- Depois abra o navegador no localhost indicado

## Ativar e usar a API
- no cmd
- ativar a Venv
- entrar na pasta API `cd API/`
- digite `python app.py` esse codigo cria automaticamente o banco de dados necessario

## Ver a API
- no navegador digite `http://127.0.0.1:5000`
- usar /plantas: "Retorna o banco completo", /solo: "Retorna os dados do solo", /nomes: "Retorna o nome_cientifico e nome_popular



