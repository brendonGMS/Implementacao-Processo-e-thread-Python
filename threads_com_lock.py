import threading

contador = 0
lock = threading.Lock()

def incrementa():
    global contador
    with lock:  # Garante que o lock será liberado
        temp = contador
        temp += 1
        contador = temp

# Lista para armazenar as threads
threads = []

try:
    # Criando e iniciando as threads
    for i in range(10):
        t = threading.Thread(target=incrementa)
        threads.append(t)
        t.start()
        print(f"Iniciada thread {i}")  # Debug

    # Esperando as threads terminarem com timeout
    for t in threads:
        t.join(timeout=2.0)  # Timeout de 2 segundos
        if t.is_alive():
            print("Aviso: Thread não terminou dentro do timeout")

except KeyboardInterrupt:
    print("\nInterrupção recebida, encerrando...")
finally:
    print(f"Contador final: {contador}")