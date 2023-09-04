def nome_e_sobrenome():
    nome = input('Insira seu nome completo')
    divide_nome = nome.split()
    primeiro_nome = divide_nome[0]
    segundo_nome = " ".join(divide_nome[1:])

    return primeiro_nome.upper() + " " + segundo_nome.lower()

print(nome_e_sobrenome())