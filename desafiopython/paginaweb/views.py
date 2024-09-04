from django.shortcuts import render
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
    personagens_traduzidos = []
    
    # Traduzir e exibir nomes e afiliações
    for personagem in personagens:
        nome = personagem.get('name', 'N/A')
        afiliacao = personagem.get('affiliation', 'N/A')
        
        nome_traduzido = translator.translate(nome, dest='pt').text
        afiliacao_traduzida = translator.translate(afiliacao, dest='pt').text
        
        personagens_traduzidos.append({
            'nome_original': nome,
            'nome_traduzido': nome_traduzido,
            'afiliacao_original': afiliacao,
            'afiliacao_traduzida': afiliacao_traduzida,
        })

    return personagens_traduzidos

def home(request):
    personagens_traduzidos = traduzir_personagens()
    context = {'personagens': personagens_traduzidos}
    return render(request,'paginainicial\home.html', context)