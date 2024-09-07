from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-4"

def product_categorizer(product_name, categories_list):
    system_prompt = f"""
        Você é um categorizador de produtos.
        Você deve assumir as categorias presentes na lista abaixo.

        # Lista de Categorias Válidas
        {categories_list.split(",")}

        # Formato da Saída
        Produto: Nome do Produto
        Categoria: apresente a categoria do produto

        # Exemplo de Saída
        Produto: Escova elétrica com recarga solar
        Categoria: Eletrônicos Verdes
    """

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": product_name
            }
        ],
        model=model,
        temperature = 0,
        max_tokens = 200
    )
    return response.choices[0].message.content

valid_categories = input("Informe as categorias válidas separando-as por vírgulas: ")

while True:
    product_name = input("Digite o nome do produto: ")
    response = product_categorizer(product_name, valid_categories)
    print(response)
