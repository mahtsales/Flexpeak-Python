age = 17

can_drive = True if age >= 18 else False # >= 18 => consegue dirigir
can_vote = True if age >= 16 else False  # >= 16 => consegue votar

# ler um valor de um pagament e aplicar um juros de 10% se o pagamento for menor que R$457,67 e 20% se for maior => operador ternário

pagamento = float(input("Digite o valor do seu pagamento: "))
juros = pagamento * 1.2 if pagamento >= 457.67 else pagamento * 1.1
print(f'O valor com juros será de: R$ {juros:.2f}')
print(f'O valor com juros será de: R$ {pagamento * 1.2 if pagamento >= 457.67 else pagamento * 1.1:.2f}')