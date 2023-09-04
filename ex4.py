def nome_maiusculo():
    texto = input('Digite seu nome completo:')
    maiuscula = texto.upper()
    return maiuscula

nome = nome_maiusculo()

print('Seu nome completo com letras maiusculas fica assim: ', nome)