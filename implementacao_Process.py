from multiprocessing import Process
import os

#Implementação de Processos

#Função Auxiliar
def info(title):
    print(title)
    print('Module name: ', __name__)
    print('Parent process: ', os.getppid()) #ID do processo pai
    print('Process id: ', os.getpid()) #ID do processo atual
    
#Função que será executada no processo filho
def f(name):
    info('function f')
    print('hello', name)
    
if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()