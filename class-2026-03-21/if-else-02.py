# ler um valor de um pagament e aplicar um juros de 10% se o pagamento for menor que R$457,67 e 20% se for maior

payment = float(input("Digite o valor do pagamento: "))
if payment < 457.67:
    payment += payment * 0.10
else:
    payment += payment * 0.20
print(f'O valor do pagamento com juros é: R${payment:.2f}')