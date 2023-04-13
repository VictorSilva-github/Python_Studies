#lista

#antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

#com Lista
notas = [7.9, 9.7, 8.2]

#Criando listas

lista = []
lista = list()
lista = [26, 'Walisson', 3.14159, False]
lista_de_lista = [10, [1,2,3]]


# indexacao e slices (fatiamente)

lista = [10, 'Victor', 3.14, True]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])


#####


lista = [10, 50, 3.14, 5, 45,60]
print(lista[0:2])
print(lista[2:4])
print("comprimento da lista: ", len(lista))




print("Lista teste com FOR")
for i in range(len(lista)):
    print("imprimindo o indece da lista: ", i)
    print("imprimindo o conteudo da lista: ",lista[i])

print("OUTRA!")
for i in range(len(lista)):
    print(" Conteudo:", lista[i], end='')