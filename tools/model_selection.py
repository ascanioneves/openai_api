from openai import OpenAI
from dotenv import load_dotenv
import os
import tiktoken
from token_counter import token_metrics

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-3.5"

encoder = tiktoken.encoding_for_model(model)

def load_data(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()
            return data
    except IOError as e:
            print(f"Error: {e}")
    
system_prompt = """
    Identifique o perfil de compra para cada cliente a seguir.

    O formato de saída deve ser:
    
    cliente - descreva o perfil do cliente em 3 palavras
"""

user_prompt = load_data("../data/lista_de_compras_100_clientes.csv")

token_list = encoder.encode(system_prompt + user_prompt)
n_tokens = len(token_list)
expected_output_length = 2048
model = "gpt-4" if n_tokens >= 4096 else model

print("Modelo escolhido: ", model)
token_metrics(model, system_prompt + user_prompt, 0.03)

response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        model=model
    )

print(response.choices[0].message.content)