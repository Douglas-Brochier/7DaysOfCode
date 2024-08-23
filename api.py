import requests
from googletrans import Translator


def traduzir_personagens():
    url = "https://last-airbender-api.fly.dev/api/v1/characters"
    
    response = requests.get(url)
    
    # Verificar se a requisição foi bem-sucedida
    if response.status_code != 200:
        print(f"Erro ao acessar a API. Status code: {response.status_code}")
        return
    
    personagens = response.json()
    
    translator = Translator()
    
    # Traduzir e exibir nomes e afiliações
    for personagem in personagens:
        nome = personagem.get('name', 'N/A')
        afiliacao = personagem.get('affiliation', 'N/A')
        
        nome_traduzido = translator.translate(nome, dest='pt').text
        afiliacao_traduzida = translator.translate(afiliacao, dest='pt').text
        
        print(f"Nome original: {nome} | Nome traduzido: {nome_traduzido}")
        print(f"Afiliação original: {afiliacao} | Afiliação traduzida: {afiliacao_traduzida}\n")

traduzir_personagens()