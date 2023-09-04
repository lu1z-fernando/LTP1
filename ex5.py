def nome_minusculo():
    texto = input('Insira seu nome completo: ')
    minusculo = texto.lower()
    return minusculo

nome = nome_minusculo()

print('Seu nome completo com letras minusculas fica assim: ' , nome)