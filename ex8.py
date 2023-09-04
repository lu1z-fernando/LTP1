def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

def contar_vogais(texto):
    texto = texto.lower()
    return sum(1 for letra in texto if letra in "aeiou")

def substituir_python_por_java(texto):
    return texto.replace("Python", "Java", -1)

def converter_para_minusculas(texto):
    return texto.lower()

def palavras_unicas(texto):
    texto = texto.lower()
    palavras = texto.split()
    palavras_unicas = set(palavras)
    return list(palavras_unicas)

def ordem_alfabetica(texto):
    palavras = texto.split()
    palavras.sort(key=lambda x: x.lower())
    return palavras

while True:
    print("\nMenu de Opções:")
    print("1. Conte o número total de palavras digitadas.")
    print("2. Conte o número de vogais na palavra digitada.")
    print("3. Substitua todas as ocorrências da palavra 'Python' por 'Java'.")
    print("4. Converta todas as letras da string para minúsculas.")
    print("5. Crie uma lista com todas as palavras únicas encontradas na string.")
    print("6. Imprima as palavras na string em ordem alfabética.")
    print("7. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        texto = input("Digite o texto: ")
        print("Número total de palavras:", contar_palavras(texto))
    elif escolha == "2":
        texto = input("Digite o texto: ")
        print("Número de vogais:", contar_vogais(texto))
    elif escolha == "3":
        texto = input("Digite o texto: ")
        novo_texto = substituir_python_por_java(texto)
        print("Texto com substituição: ", novo_texto)
    elif escolha == "4":
        texto = input("Digite o texto: ")
        texto_minusculo = converter_para_minusculas(texto)
        print("Texto em minúsculas: ", texto_minusculo)
    elif escolha == "5":
        texto = input("Digite o texto: ")
        palavras = palavras_unicas(texto)
        print("Palavras únicas encontradas:", palavras)
    elif escolha == "6":
        texto = input("Digite o texto: ")
        palavras_ordenadas = ordem_alfabetica(texto)
        print("Palavras em ordem alfabética:", palavras_ordenadas)
    elif escolha == "7":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")