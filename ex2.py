def conta_caractere():
    frase = input("Digite uma frase: ")
    quantidade_caractere = len(frase)
    return quantidade_caractere

qtd = conta_caractere()
print("A frase possui", qtd , "caractere(s)!")