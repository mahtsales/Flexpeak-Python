pessoas = { #nesse set(lista), nós especificamos de maneira detalhada o que desejamos.
    "Nome" : 'Matheus',
    "Idade" : 21,
    "Cidade" : 'Manaus'
}
print(pessoas)

nomes = ['Matheus', 'João', 'Maria'] #set(lista) somente de nomes
print(nomes)
print(nomes[0])

nomes.append('Davi') #.append => add um item no fim da lista
print(nomes)

nomes.insert(1, 'Alvaro') #.insert => add um item na posicao especifica
print(nomes)
