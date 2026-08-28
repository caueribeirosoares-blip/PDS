# 1. Lista de nomes de estudantes
estudantes = ["Carlos", "Ana", "Pedro", "Beatriz", "Mariana"]

# Use sort() para ordenar diretamente a lista original em ordem decrescente
estudantes.sort(reverse=False)
print("Estudantes ordenados (decrescente):", estudantes)

# Exemplo de lista original
lista_original = [5, 2, 9, 1, 74]

# 1. Ordenação crescente (padrão)
lista_crescente = sorted(lista_original)

# 2. Ordenação decrescente (ajustando o reverse)
lista_decrescente = sorted(lista_original, reverse=True)

# 3. Impressão das listas para conferência
print("Lista original:", lista_original)
print("Ordem crescente:", lista_crescente)
print("Ordem decrescente:", lista_decrescente)
