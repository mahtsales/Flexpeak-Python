#Crie uma funcao para calcular a media:

def calcular_media():
    media = (nota1 + nota2) / 2
    print(f'Sua media será de: {media:.2f}')

nota1 = float(input("digite a sua 1º nota: "))
nota2 = float(input("digite a sua 2º nota: "))

calcular_media() #chamar == instanciar 