from django.shortcuts import render
import requests
from googletrans import Translator
from .models import Personagem

def traduzir_personagens():
    url = "https://last-airbender-api.fly.dev/api/v1/characters"
    
    response = requests.get(url)
    
    # Verificar se a requisição foi bem-sucedida
    if response.status_code != 200:
        print(f"Erro ao acessar a API. Status code: {response.status_code}")
        return
    
    personagens = response.json()
    
    translator = Translator()
    
    # Traduzir nomes e afiliações
    for personagem in personagens:
        nome = personagem.get('name', 'N/A')
        afiliacao = personagem.get('affiliation', 'N/A')
        
        nome_traduzido = translator.translate(nome, dest='pt').text
        afiliacao_traduzida = translator.translate(afiliacao, dest='pt').text
        
        # Salvando os personagens no banco de dados
        Personagem.objects.create(
            nome_original=nome,
            nome_traduzido=nome_traduzido,
            afiliacao_original=afiliacao,
            afiliacao_traduzida=afiliacao_traduzida
        )

def home(request):
    traduzir_personagens() 
    personagens_traduzidos = Personagem.objects.all()  # Busca todos os personagens salvos
    context = {'personagens': personagens_traduzidos}
    return render(request,'paginainicial\home.html', context)