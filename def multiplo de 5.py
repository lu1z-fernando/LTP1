# Exercício 1: Faça uma função que recebe um número e retorna True se ele é múltiplo de 5 ou False caso contrário.

def multiplo_5(numero):
    if numero % 5 == 0:
        print("o numero é multiplo de 5")
        return True
    else: 
        print("o numero não é multiplo de 5")
        return False
    
valor = int(input("digite um numero inteiro: "))

print( multiplo_5(valor))
