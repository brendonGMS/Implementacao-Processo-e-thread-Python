from codigo import sensor_temperatura, sensor_umidade, sensor_luminosidade, processar_alertas
import multiprocessing
import threading
import time
import signal
import sys

def encerrar_sistema(signum, frame):
    """Handler para encerramento gracioso"""
    print("\nRecebido sinal de desligamento, finalizando...")
    processo_alerta.terminate()
    sys.exit(0)

def main():
    global processo_alerta  # Tornando global para o signal handler
    
    # Configura handler para Ctrl+C
    signal.signal(signal.SIGINT, encerrar_sistema)
    
    # Threads para os sensores
    threads = [
        threading.Thread(target=sensor_temperatura, name="Sensor-Temperatura"),
        threading.Thread(target=sensor_umidade, name="Sensor-Umidade"),
        threading.Thread(target=sensor_luminosidade, name="Sensor-Luminosidade")
    ]
    
    # Processo para alertas
    processo_alerta = multiprocessing.Process(
        target=processar_alertas,
        name="Processo-Alertas"
    )
    
    # Iniciar threads
    for t in threads:
        t.daemon = True
        t.start()
        print(f"Iniciada {t.name}")
    
    # Iniciar processo
    processo_alerta.start()
    print(f"Iniciado {processo_alerta.name}")
    
    # Mensagem inicial
    print("\n" + "="*50)
    print("Sistema de Monitoramento de Estufa Inteligente")
    print("="*50)
    print("\n• Sensores em operação")
    print(f"• Processo de alertas ativo (PID: {processo_alerta.pid})")
    print("\nPressione Ctrl+C para encerrar\n")
    
    # Loop principal
    try:
        while True:
            time.sleep(0.5)  # Verificação mais frequente
            
            # Verifica se algum thread morreu
            for t in threads:
                if not t.is_alive():
                    print(f"ERRO: {t.name} parou inesperadamente!")
                    encerrar_sistema(None, None)
                    
    except Exception as e:
        print(f"Erro fatal: {str(e)}")
        encerrar_sistema(None, None)

if __name__ == "__main__":
    main()