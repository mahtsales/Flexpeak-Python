from peoples import pessoas

for chave in pessoas:
    print (chave)

for chave, valor in pessoas.items():
    print(valor["nome"], valor["idade"])
