from codigo import sensor_temperatura, sensor_umidade, sensor_luminosidade, processar_alertas
import multiprocessing
import threading
import time

def main():
    # Configura threads para os sensores
    sensores = [
        threading.Thread(target=sensor_temperatura, daemon=True),
        threading.Thread(target=sensor_umidade, daemon=True),
        threading.Thread(target=sensor_luminosidade, daemon=True)
    ]
    
    # Inicia processo de alertas
    alertas = multiprocessing.Process(target=processar_alertas, daemon=True)
    alertas.start()
    
    # Inicia threads dos sensores
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