# Exercício 2: Faça uma função que recebe um número e imprime no console se ele é múltiplo de 5 e de 3 ou False caso contrário
def multiplo_de_3_e_5(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        print("o numero é multiplo de 5 e 3!")
        return True
    else:
        print("o numero não é multiplo!")
        return False
    
valor = int(input("Digite um número inteiro: "))

print(multiplo_de_3_e_5(valor))


    
    