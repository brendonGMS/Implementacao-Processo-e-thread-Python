import threading  # Importa o módulo para trabalhar com threads
import multiprocessing  # Importa o módulo para trabalhar com processos
import random  # Importa o módulo para gerar números aleatórios
import time  # Importa o módulo para manipular tempo e pausas
from datetime import datetime  # Importa para obter data e hora atuais

# Cria um lock para garantir que apenas uma thread imprima por vez (evita prints misturados)
log_lock = threading.Lock()

# Função para criar uma fila de alertas compartilhada entre processos
def criar_fila_alertas():
    """Cria e retorna uma fila de alertas compartilhada"""
    return multiprocessing.Queue()

# Função que simula um sensor de temperatura
def sensor_temperatura(alertas, intervalo=0.5):
    """Simula leituras de temperatura a cada 0.5s"""
    while True:
        valor = random.uniform(15.0, 35.0)  # Gera valor aleatório de temperatura
        timestamp = datetime.now().strftime('%H:%M:%S')  # Pega horário atual
        
        # Garante que o print não seja interrompido por outra thread
        with log_lock:
            print(f'[{timestamp}] Temperatura: {valor:.1f}°C')
            
        # Se a temperatura for maior que 25°C, envia alerta para a fila
        if valor > 25.0:
            alertas.put(f'ALERTA: Temperatura alta {valor:.1f}°C às {timestamp}')
            
        time.sleep(intervalo)  # Aguarda o intervalo antes da próxima leitura

# Função que simula um sensor de umidade
def sensor_umidade(alertas, intervalo=1.0):
    """Simula leituras de umidade a cada 1s"""
    while True:
        try:
            valor = random.uniform(40.0, 90.0)  # Gera valor aleatório de umidade
            
            # Verifica se o valor é realmente um número (proteção extra)
            if not isinstance(valor, (int, float)):
                print(f"Valor realmente inválido detectado: {valor} (Tipo: {type(valor)})")
                continue
                
            timestamp = datetime.now().strftime("%H:%M:%S")  # Pega horário atual
            
            # Garante que o print não seja interrompido por outra thread
            with log_lock:
                print(f"[{timestamp}] Umidade: {valor:.1f}%")
            
            # Se a umidade for menor que 50%, envia alerta para a fila
            if valor < 50.0:
                alertas.put(f"ALERTA: Umidade baixa {valor:.1f}% às {timestamp}")
            
            time.sleep(intervalo)  # Aguarda o intervalo antes da próxima leitura
            
        except Exception as e:
            # Em caso de erro, exibe mensagem e espera 1 segundo antes de tentar novamente
            print(f"Erro no sensor de umidade: {str(e)}")
            time.sleep(1)

# Função que simula um sensor de luminosidade
def sensor_luminosidade(alertas, intervalo=1.5):
    """Simula leituras de luminosidade a cada 1.5s"""
    while True:
        valor = random.uniform(0.0, 100.0)  # Gera valor aleatório de luminosidade
        timestamp = datetime.now().strftime('%H:%M:%S')  # Pega horário atual
        
        # Garante que o print não seja interrompido por outra thread
        with log_lock:
            print(f'[{timestamp}] Luminosidade: {valor:.1f}%')
            
        # Se a luminosidade for menor que 30%, envia alerta para a fila
        if valor < 30.0:
            alertas.put(f'ALERTA: Luminosidade baixa {valor:.1f}')
            
        time.sleep(intervalo)  # Aguarda o intervalo antes da próxima leitura

# Função que processa os alertas recebidos na fila
def processar_alertas(alertas):
    """Processo separado para lidar com alertas"""
    while True:
        # Se houver alertas na fila, pega e imprime o alerta
        if not alertas.empty():
            alerta = alertas.get()
            print(f"\n⚠️ {alerta}\n")
        time.sleep(0.1)  # Aguarda um pouco antes de verificar novamente