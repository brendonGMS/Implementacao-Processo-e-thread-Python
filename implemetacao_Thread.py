import threading 
import time

#Implementação de Threads
def tarefa(nome):
    print(f'Thread {nome} iniciada.')
    time.sleep(2)
    print(f'Thread {nome} finalizada')
    
t1 = threading.Thread(target=tarefa, args=('1'))
t2 = threading.Thread(target=tarefa, args=('2'))

#Iniciando as threads
t1.start()
t2.start()

#Esperando as threads
t1.join()
t2.join()

print('Todas as threads terminaram')