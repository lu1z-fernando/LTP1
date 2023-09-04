def armazena_nome(nome):
    
    parte_nome = nome.split()
    nome_usuario = parte_nome[0]
    sobrenome_usuario = " ".join(parte_nome[1:])
    nome_completo = nome.upper()
    tamanho_completo_nome = len(nome)

    print('Nome: ' , nome_completo.lower())
    print('tem ', tamanho_completo_nome , 'caractere(s)')

armazena_nome(input('Digite seu nome completo (evite espaços)!'))