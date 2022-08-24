import threading


def counter():  # definindo a função de contador
    for i in range(1, 101):
        print('Contando...', i)


# criando a thread
t1 = threading.Thread(target=counter)

# iniciando a thread
t1.start()

# comando que bloqueia a continuação do codigo ate que a thread seja finalizada, caso esse comando seja comentado o restante do codigo vai ser executado enquanto a thread executa em paralelo
t1.join()

print("Programa finalizado")
