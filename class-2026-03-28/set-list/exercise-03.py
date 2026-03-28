#realizar a remocao do nome 'Bianca' da lista abaixo:
peoples = ['Bianca', 'Alvaro', 'Enzo', 'Davi', 'Bianca', 'Bianca']
for nome in peoples [:]: #vai removendo de maneira gradativa
    if nome == 'Bianca':
        peoples.remove(nome)
        print(peoples)


