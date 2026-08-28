# --- 1. Entrada de Dados (Built-ins iniciais) ---

# Solicita a quantidade de tarefas e converte para inteiro
qtd_tarefas = int(input("Quantas tarefas deseja cadastrar? "))

# Lista para armazenar os nomes textuais das tarefas
lista_tarefas = []

# Estrutura de repetição para capturar os nomes das tarefas
for i in range(qtd_tarefas):
    nome = input(f"Digite o nome da tarefa {i + 1}: ")
    lista_tarefas.append(nome)


# --- 2. Processamento com enumerate() e range() ---

# Nova lista que armazenará as tuplas estruturadas
banco_dados_tarefas = []

# Percorre a lista_tarefas obtendo o índice (iniciando em 1) e o nome
for id_tarefa, nome_tarefa in enumerate(lista_tarefas, start=1):
    
    # Cálculo do prazo estimado baseado no índice (Ex: tarefa 1 = 2 dias, tarefa 2 = 4 dias)
    prazo_dias = id_tarefa * 2
    
    # Status inicial padronizado
    status = "Pendente"
    
    # Criação da tupla estruturada
    tarefa_tupla = (id_tarefa, nome_tarefa, prazo_dias, status)
    
    # Armazenamento no banco de dados fictício
    banco_dados_tarefas.append(tarefa_tupla)


# --- 3. Saída de Dados e Desempacotamento ---

print("\n--- RESUMO DAS TAREFAS CADASTRADAS ---")

# Percorre o banco de dados para exibir as informações
for tarefa in banco_dados_tarefas:
    # Realiza o desempacotamento de tuplas (evitando acesso por índices como tarefa[0])
    id_t, nome_t, prazo_t, status_t = tarefa
    
    # Exibição formatada no console
    print(f"ID: {id_t} | Tarefa: {nome_t} | Prazo: {prazo_t} dias | Status: {status_t}")

print("-" * 38)

# Exibe a quantidade total de tarefas processadas usando len()
total_processadas = len(banco_dados_tarefas)
print(f"Quantidade total de tarefas processadas com sucesso: {total_processadas}")
