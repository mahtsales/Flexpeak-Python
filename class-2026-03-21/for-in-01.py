#leiam uma palavra e verifiquem se ela contem vogais, se sim, imprima as vogais contidas nela:

palavra = str(input("Digite uma palavra: "))
vogais = "aeiou"
for letra in palavra:
    if letra in vogais:
        print(letra)
    else:
        print("Palavra inválida. Digite corretamente.")