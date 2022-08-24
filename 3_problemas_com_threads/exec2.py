import time
import threading

teste = time.time()


def fruit_printer(fruit):
    time_end = time.time() + 3
    while time.time() < time_end:
        print(fruit)


# criando a thread
t1 = threading.Thread(target=fruit_printer, args=('Morango',))
t2 = threading.Thread(target=fruit_printer, args=('Uva',))
t3 = threading.Thread(target=fruit_printer, args=('Laranja',))

# iniciando as threads
t1.start()
t2.start()
t3.start()


print("Programa finalizado")
