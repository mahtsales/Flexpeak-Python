#METODO DO PROFESSOR

inicio = int(input('Digite o numero que queira iniciar: '))
termino = int(input('Digite o numero que queira terminar: '))
passo = int(input('Digite quantos passos desejar dar (incremento): '))

if passo == 0:
    print("O passo não pode ser zero.")
else:
    if termino == inicio:
        print("Valores iguais, não ocorre loop.")
    else:
        if (termino < inicio and passo > 0) or (termino > inicio and passo < 0):
            print("Valor inválido.")
        else:
            for i in range (inicio, termino, passo):
                print(i)