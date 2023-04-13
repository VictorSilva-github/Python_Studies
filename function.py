

# 1. FUNCOES

#print() # - Imprimir uma mensagem (int, float, str) no console (terminal, cmd)
#input() # - Retorna um dado informado pelo usuario. (entrada padrao) e pode receber uma string
#len() # - Recebe uma lista e rotorna o tamanho dessa lista
#max() # - Retorna o maior valor de uma lista

def welcome():
    print("Seja bem vindo CARAIO")
    print("ola, voce vai conseguir sim!!!")


welcome()
welcome()
welcome()

#valores sem definicao
def welcome(name, curso):
    print(f"Seja bem vindo, {name}!")
    print(f"ola, voce vai conseguir sim!!! esse {curso}, vai ser top")

welcome("Victor","Python")




#valor definido, curso de algo
def welcome(name, curso="Python"):
    print(f"Seja bem vindo, {name}!")
    print(f"ola, voce vai conseguir sim!!! esse {curso}, vai ser top")


welcome("Victor")



def soma(num1, num2):
    return num1 + num2

resultado = soma(5,7)
print("O resultador foi: ", resultado)


def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1+num2
    
    elif operacao == '-':
        return num1-num2
    
    elif operacao== '*':
        return num1*num2

resultado = calculadora(10, 20)
print(resultado) 