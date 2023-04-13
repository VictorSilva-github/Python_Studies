numero_sorteado = 15
contador = 0
"""
if numero_sorteado == numero_escolhido:
    print("Voce acertou!")
else:
    print('Voce errou!')
"""

for i in range(10): # 0 ate 9
            print(i)
print("outro LOOP")
for i in range(1, 11): # 1 ate 10
            print(i)

print("outro LOOP EM 2 EM 2")
for i in range(0, 10, 2): # vai do 1 ao 10 EM 2 em 2
            print(i)



numero_escolhido = int(input("Informe um numero entre 1 e 20: "))

while numero_escolhido != numero_sorteado:
        print("Voce errou o numero, tente novamente! ")
        numero_escolhido = int(input("Informe um numero entre 1 e 20: "))
  
print("Parabens, Voce acertou! Hello world, o numero sorteado foi: ", numero_sorteado)


    


 