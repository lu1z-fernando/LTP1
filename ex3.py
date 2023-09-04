def contador_letras(letra): 
    nome = input('Digite seu nome Completo ').lower() 
    return  nome.count(letra)

contador = 'a' 
print('O nome inserido contem ' , contador_letras(contador), 'letra(S)' , contador)