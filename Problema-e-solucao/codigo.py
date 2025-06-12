import threading
import multiprocessing
import random
import time
from datetime import datetime

#Dados compartilhados

alertas = multiprocessing.Queue()
log_lock = threading.Lock()

def sensor_temperatura(intervalo=0.5):
    while True:
        valor = random.uniform(15.0, 35.0)
        timestamp = datetime.now().strftime('%H:%M:%S.%f')
        
        with log_lock:
            print(f'[{timestamp}] Temperatura: {valor:.1f}°C às {timestamp}')
            
        if valor > 25.0:
            alertas.put(f'ALERTA: Temperatura alta {valor:.1f}°C às {timestamp}')
            
        time.sleep(intervalo)
        
def sensor_umidade(intervalo=1.0):
    """Simula leituras de umidade a cada 1s"""
    while True:
        try:
            # Geração do valor com verificação explícita
            valor = random.uniform(40.0, 90.0)
            
            # Verificação robusta do tipo
            if not isinstance(valor, (int, float)):
                print(f"Valor realmente inválido detectado: {valor} (Tipo: {type(valor)})")
                continue  # Pula para a próxima iteração
                
            timestamp = datetime.now().strftime("%H:%M:%S.%f")
            
            with log_lock:
                print(f"[{timestamp}] Umidade: {valor:.1f}%")
            
            # Comparação simplificada e segura
            if valor < 50.0:
                alertas.put(f"ALERTA: Umidade baixa {valor:.1f}% às {timestamp}")
            
            time.sleep(intervalo)
            
        except Exception as e:
            print(f"Erro no sensor de umidade: {str(e)}")
            time.sleep(1)
            
def sensor_luminosidade(intervalo=1.5):
    while True:
        valor = random.uniform(0.0, 100.0)
        timestamp = datetime.now().strftime('%H:%M:%S.%f')
        
        with log_lock:
            print(f'[{timestamp}] Luminosidade: {valor:.1f}%')
            
        if valor < 30.0:
            alertas.put(f'ALERTA: Luminosidade baixa {valor:.1f}')
            
        time.sleep(intervalo)

def processar_alertas():
    """Processo separado para lidar com alertas"""
    while True:
        if not alertas.empty():
            alerta = alertas.get()
            print(f"\n⚠️ {alerta}\n")
        time.sleep(0.1)