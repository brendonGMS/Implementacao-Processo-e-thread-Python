from codigo import sensor_temperatura, sensor_umidade, sensor_luminosidade, processar_alertas, criar_fila_alertas
import threading  # Importa o módulo para trabalhar com threads
import multiprocessing  # Importa o módulo para trabalhar com processos
import time  # Importa o módulo para manipular tempo e pausas

def main():
    # Cria a fila de alertas no processo principal (compartilhada entre threads e processos)
    alertas = criar_fila_alertas()
    
    # Cria as threads para os sensores de temperatura, umidade e luminosidade
    sensores = [
        threading.Thread(target=sensor_temperatura, args=(alertas,), daemon=True),  # Thread para sensor de temperatura
        threading.Thread(target=sensor_umidade, args=(alertas,), daemon=True),      # Thread para sensor de umidade
        threading.Thread(target=sensor_luminosidade, args=(alertas,), daemon=True)  # Thread para sensor de luminosidade
    ]
    
    # Cria um processo separado para processar os alertas recebidos
    alertas_process = multiprocessing.Process(target=processar_alertas, args=(alertas,), daemon=True)
    alertas_process.start()  # Inicia o processo de alertas
    
    # Inicia todas as threads dos sensores
    for sensor in sensores:
        sensor.start()
    
    print("Sistema iniciado. Pressione Ctrl+C para parar.")
    
    try:
        # Mantém o programa principal rodando até que o usuário pressione Ctrl+C
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Ao pressionar Ctrl+C, exibe mensagem de encerramento
        print("\nEncerrando o sistema...")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()