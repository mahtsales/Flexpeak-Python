#Escreva um número que leia um numero e o imprima caso ele seja maior
#que 20 anos, caso contrário, escreva 'feliz aniversário marcos'

#numero = int(input('Digite o número:'))

#if numero >= 20:
#    print(numero)
#else:
#    print('feliz aniversario, Marcos!')



#0 a 4.9 = reprovado
#5.0 a 6.9 = recuperacao
#7.0 a 10.0 = aprovado

nota1 = float (input ('Digite a primeira nota: '))
nota2 = float (input ('Digite a segunda nota: '))
nota3 = float (input ('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print(f"A sua média é {media:.2f}")

#sempre inicia a estrutura de condição do maior para o menor.

if media == 10:
    print('Você é foda, parabéns!')
elif media >= 9 and media <= 10:
    print('Aprovado.')
elif media >= 5 and media < 7:
    print('Recuperação.')
elif media >= 0 and media <=4.9:
    print('Reprovado com sucesso.')
else:
    print('Corrija o valor inserido.')