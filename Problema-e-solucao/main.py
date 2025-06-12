from codigo import sensor_temperatura, sensor_umidade, sensor_luminosidade, processar_alertas
import multiprocessing
import threading
import time

def main():
    # Threads para os sensores (I/O bound)
    threads = [
        threading.Thread(target=sensor_temperatura),
        threading.Thread(target=sensor_umidade),
        threading.Thread(target=sensor_luminosidade)
    ]
    
    # Processo para alertas (CPU bound)
    processo_alerta = multiprocessing.Process(target=processar_alertas)
    
    # Iniciar tudo
    for t in threads:
        t.daemon = True  # Permite terminar com Ctrl+C
        t.start()
    
    processo_alerta.start()
    
    print("Sistema de monitoramento iniciado. Pressione Ctrl+C para parar.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nEncerrando o sistema...")
        processo_alerta.terminate()

if __name__ == "__main__":
    main()