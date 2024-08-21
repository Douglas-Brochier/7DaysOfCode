# DAY1
# Criar o código Python para executar uma requisição HTTP do tipo GET usando o módulo requests.
# Executar a requisição e pegar a resposta (o JSON).
# Imprimir o corpo da resposta através de um print.

import requests

url = 'https://last-airbender-api.fly.dev/api/v1/characters'

response = requests.get(url)

if response.status_code == 200:
    print('Resposta:', response.json())
else:
    print(f'Erro na requisição. Status code: {response.status_code}')