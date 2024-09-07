from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-4"

def load_data(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()
            return data
    except IOError as e:
            print(f"Error: {e}")

def save_data(filename, content):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")

def sentiment_analyzer(product):
    system_prompt = f"""
        Você é um analisador de sentimentos de avaliações de produtos.
        Escreva um parágrafo com até 50 palavras resumindo as avaliações e 
        depois atribua qual o sentimento geral para o produto.
        Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

        # Formato de Saída

        Nome do Produto:
        Resumo das Avaliações:
        Sentimento Geral: [utilize aqui apenas Positivo, Negativo ou Neutro]
        Ponto fortes: lista com três bullets
        Pontos fracos: lista com três bullets
    """
    user_prompt = load_data(f"../data/avaliacoes-{product}.txt")
    print(f"A Análise de sentimentos do produto {product} foi iniciada!")

    response = client.chat.completions.create(
        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        model = model
    )
    save_data(f"../data/analise-{product}.txt", response.choices[0].message.content)

sentiment_analyzer("Maquiagem mineral")