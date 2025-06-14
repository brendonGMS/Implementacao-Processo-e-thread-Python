from codigo import sensor_temperatura, sensor_umidade, sensor_luminosidade, processar_alertas
import threading
import multiprocessing
import time

def main():
    sensores = [
        threading.Thread(target=sensor_temperatura, daemon=True),
        threading.Thread(target=sensor_umidade, daemon=True),
        threading.Thread(target=sensor_luminosidade, daemon=True)
    ]
    
    alertas = multiprocessing.Process(target=processar_alertas, daemon=True)
    alertas.start()
    
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
