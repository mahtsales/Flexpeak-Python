#verificar se um número é par ou ímpar
number = int(input("Digite um número inteiro: "))
if number % 2 == 0:  # Verifica se o número é par
    print(f"O número {number} é par.")
else:
    print(f"O número {number} é ímpar.")

#verificar se um número é positivo, negativo ou zero
number = float(input("Digite um número: "))
if number > 0:
    print(f"o número {number}é positivo.")
elif number < 0:
    print(f"O número {number} é negativo.")
else:    
    print("O número é zero.")

#escrever tres numero e mostrar o maior
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 >= num2 and num1 >= num3:
    print(f"O maior número é: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"O maior número é: {num2}")
else:
    print(f"O maior número é: {num3}")

#verificar idade e mostra se pode votar ou nao

age = int(input("Digite sua idade: "))
if age >= 18:
    print('você pode votar.')
elif age > 16 and age < 18:
    print('pode votar, mas não é obrigatório.')
else:
    print('você não pode votar.')