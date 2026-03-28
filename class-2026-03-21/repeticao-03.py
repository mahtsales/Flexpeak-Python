#usuário digite entrada, saida, passo, e o programa imprima a contagem de acordo com os dados inseridos:

inicio = int(input('Digite o numero que queira iniciar: '))
termino = int(input('Digite o numero que queira terminar: '))
passo = int(input('Digite quantos passos desejar dar (incremento): '))

if passo == 0:
    print('O passo não pode ser zero. Insire outro valor')
else:
    if passo > 0 and inicio < termino:
        for valores in range(inicio, termino + 1, passo):
            print(valores)
    elif passo < 0 and inicio > termino:
        for valores in range(inicio, termino - 1, passo):
            print(valores)
    else:
        print('A combinação de início, término e passo não é válida.')