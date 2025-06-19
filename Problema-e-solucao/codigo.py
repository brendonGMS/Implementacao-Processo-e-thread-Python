import threading
import multiprocessing
import random
import time
from datetime import datetime


log_lock = threading.Lock()

def criar_fila_alertas():
    """Cria e retorna uma fila de alertas compartilhada"""
    return multiprocessing.Queue()

def sensor_temperatura(alertas, intervalo=0.5):
    """Simula leituras de temperatura a cada 0.5s"""
    while True:
        valor = random.uniform(15.0, 35.0)
        timestamp = datetime.now().strftime('%H:%M:%S')
        
        with log_lock:
            print(f'[{timestamp}] Temperatura: {valor:.1f}°C')
            
        if valor > 25.0:
            alertas.put(f'ALERTA: Temperatura alta {valor:.1f}°C às {timestamp}')
            
        time.sleep(intervalo)
        
def sensor_umidade(alertas, intervalo=1.0):
    """Simula leituras de umidade a cada 1s"""
    while True:
        try:
            valor = random.uniform(40.0, 90.0)
            
            if not isinstance(valor, (int, float)):
                print(f"Valor realmente inválido detectado: {valor} (Tipo: {type(valor)})")
                continue
                
            timestamp = datetime.now().strftime("%H:%M:%S")
            
            with log_lock:
                print(f"[{timestamp}] Umidade: {valor:.1f}%")
            
            if valor < 50.0:
                alertas.put(f"ALERTA: Umidade baixa {valor:.1f}% às {timestamp}")
            
            time.sleep(intervalo)
            
        except Exception as e:
            print(f"Erro no sensor de umidade: {str(e)}")
            time.sleep(1)
            
def sensor_luminosidade(alertas, intervalo=1.5):
    """Simula leituras de luminosidade a cada 1.5s"""
    while True:
        valor = random.uniform(0.0, 100.0)
        timestamp = datetime.now().strftime('%H:%M:%S')
        
        with log_lock:
            print(f'[{timestamp}] Luminosidade: {valor:.1f}%')
            
        if valor < 30.0:
            alertas.put(f'ALERTA: Luminosidade baixa {valor:.1f}')
            
        time.sleep(intervalo)

def processar_alertas(alertas):
    """Processo separado para lidar com alertas"""
    while True:
        if not alertas.empty():
            alerta = alertas.get()
            print(f"\n⚠️ {alerta}\n")
        time.sleep(0.1)