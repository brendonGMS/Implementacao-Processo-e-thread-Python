from codigo import sensor_temperatura, sensor_umidade, sensor_luminosidade, processar_alertas, criar_fila_alertas
import threading
import multiprocessing
import time

def main():
    # Cria a fila de alertas no processo principal
    alertas = criar_fila_alertas()
    
    sensores = [
        threading.Thread(target=sensor_temperatura, args=(alertas,), daemon=True),
        threading.Thread(target=sensor_umidade, args=(alertas,), daemon=True),
        threading.Thread(target=sensor_luminosidade, args=(alertas,), daemon=True)
    ]
    
    alertas_process = multiprocessing.Process(target=processar_alertas, args=(alertas,), daemon=True)
    alertas_process.start()
    
    for sensor in sensores:
        sensor.start()
    
    print("Sistema iniciado. Pressione Ctrl+C para parar.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nEncerrando o sistema...")

if __name__ == "__main__":
    main()