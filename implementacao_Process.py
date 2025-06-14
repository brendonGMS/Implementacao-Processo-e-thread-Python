from multiprocessing import Process

def tarefa():
    print("Executando em um processo separado.")

# Criando o processo
p = Process(target=tarefa)

# Iniciando o processo
p.start()

# Esperando o processo terminar
p.join()
