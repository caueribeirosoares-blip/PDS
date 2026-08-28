class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}"

# Solicita os dados ao usuário
titulo_informado = input("Digite o título do livro: ")
autor_informado = input("Digite o autor do livro: ")
paginas_informadas = input("Digite a quantidade de páginas: ")

# Cria a instância do livro
novo_livro = Livro(titulo_informado, autor_informado, paginas_informadas)

# Exibe a descrição formatada utilizando o método __str__
print("\n--- Conferência dos Dados ---")
print(novo_livro)
