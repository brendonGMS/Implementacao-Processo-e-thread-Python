from multiprocessing import Pool
import time
def tarefa_pesada(x):
    return sum(i * i for i in range(10**2))

def executar_serial():
    inicio = time.time()
    results = [tarefa_pesada(x) for x in range(10)]
    tempo = time.time() - inicio
    print(f'Serial:{tempo:.4f} segundos')
    return results, tempo

def executar_paralelo(num_processso=4):
    inicio = time.time()
    with Pool(processes=num_processso) as pool:
        results = pool.map(tarefa_pesada, range(10))
    tempo = time.time() - inicio
    print(f'Paralelo ({num_processso} processos): {tempo:.4f} segundos')
    return results, tempo 

if __name__ == '__main__':
    print('=== Comparação Serial vs Paralelo ===')
    resultados_serial, tempo_serial = executar_serial()
    
    # Execução paralela com diferentes números de processos
    for n in [2, 4, 8]:
        resultados_paralelo, tempo_paralelo = executar_paralelo(n)
        
        # Verifica se os resultados são iguais
        assert resultados_serial == resultados_paralelo, "Resultados diferentes!"
        
        # Calcula speedup
        speedup = tempo_serial / tempo_paralelo
        print(f"Speedup ({n} processos): {speedup:.2f}x")
    
    print("\nOs resultados foram verificados como idênticos em ambas abordagens.")