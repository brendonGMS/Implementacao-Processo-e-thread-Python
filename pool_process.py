from multiprocessing import Pool
import time

def quadrado(x):
    return x * x

if __name__ == '__main__':
    with Pool(processes=4) as pool: #Cria um pool com 4 processos
        #Divide o trabalho entre os processos
        results = pool.map(quadrado, range(10))
        print(results)