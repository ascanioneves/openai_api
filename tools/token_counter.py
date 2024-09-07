import tiktoken

def token_metrics(model, text, price):
    encoder = tiktoken.encoding_for_model(model)
    token_list = encoder.encode(text)

    print("Lista de Tokens: ", token_list)
    print("Quantos tokens temos: ", len(token_list))
    print(f"Custo para o modelo {model} é de ${(len(token_list)/1000) * price}")

token_metrics("gpt-4", "Você é um categorizador de produtos.", 0.03)
print("\n")
token_metrics("gpt-3.5-turbo-1106", "Você é um categorizador de produtos.", 0.001)