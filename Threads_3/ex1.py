import threading
import time


class quantosPrimos(threading.Thread):
    def __init__(self, nomeThread, inicio, fim):
        threading.Thread.__init__(self)
        self.inicio = inicio
        self.fim = fim
        self.total = inicio - fim
        self.nomeThread = nomeThread

    def run(self):

        primos = []

        for num in range(self.inicio, self.fim):

            isPrimo = True
            i = 2

            while (i*i) <= num:

                if (num % i) == 0:
                    isPrimo = False
                    break

                i += 1

            if (isPrimo and num > 1):
                primos.append(num)

                qtdPrimos = len(primos)
                if (qtdPrimos % 20000 == 0):
                    progresso = round(((self.inicio-num)*100)/self.total, 2)
                    print(self.nomeThread+' achou '+str(qtdPrimos) +
                          ' primos ate agora - '+str(progresso)+'% do range percorrido')

        qtdPrimos = len(primos)
        print(self.nomeThread + ' achou ' + str(qtdPrimos)+' primos entre ' +
              str(self.inicio)+' e '+str(self.fim))
        if (qtdPrimos > 0):
            print('Sendo eles: ', primos)
        print(qtdPrimos)


calculo1 = quantosPrimos('Calculo 1', 1000000, 30000000)
calculo2 = quantosPrimos('Calculo 2', 90000000, 120000000)

tempoInicio = time.time()

calculo1.start()
calculo2.start()

calculo1.join()
calculo2.join()

tempoTotal = round((time.time() - tempoInicio), 3)
print('Tempo total de processamento: '+str(tempoTotal)+' segundos')
