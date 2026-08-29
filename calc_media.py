def calcular_media(numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma / len(numeros)

# Lista de números
numeros = [10, 20, 30, 40, 50]

# Chamando a função
media = calcular_media(numeros)

print(f"A média é: {media:.2f}")
