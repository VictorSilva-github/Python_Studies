# metodo de lista

lista = [1, 3, 12, 8, 2]

#append

print("Antes do append: ", lista)

lista.append(3)

print("Depois do append: ", lista)

#insert


lista.insert(2, 10)
print("Depois do INSERT: ", lista)

#extend

lista2 = [100, 300, 1200, 800, 200]
lista.extend(lista2)

print("Depois do extend: ",lista)


##### POP
lista.pop(0)
print("Depois do POP: ",lista)




##### REMOVE ele vai procurar o valor dentro do remove e remover
lista.remove(3)
print("Depois do REMOVE: ",lista)



##### COUNT
print("Quantidade de 2 na lista: ",lista.count(2))


##### index
print("Qual o indice do elemento 12: ",lista.index(12))


##### SORT organizar em ordem
lista.sort()
print("A ordem correta seria... ",lista)
lista.sort(reverse=True)
print("A ordem correta de tras pra frente... ",lista)

print("A soma da lista ",sum(lista))

print("A Minimo da lista ",max(lista))
print("A Maximo da lista ",min(lista))