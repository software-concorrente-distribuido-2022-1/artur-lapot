import time
import numpy
import threading
from typing import List


class ArrayMultithreading:

    def searcher(self, x: int, index: int, a: List[int], resultado):
        threadAtual = threading.current_thread()

        for i, value in enumerate(a):

            if(len(resultado) > 0):
                print('Parando '+threadAtual.name+' em i='+str(i))
                break

            if (value == x):
                resultado.append(i+index)
                print('Encontrado o valor na '+threadAtual.name)
                break

            time.sleep(0.0001)

    def parallelSearch(self, x: int, a: List[int], numThreads: int):
        threads = []
        resultado = []
        index = 0

        divisoes = numpy.array_split(a, numThreads)

        for array in divisoes:
            arraySize = len(array)

            if (arraySize > 0):
                thread = threading.Thread(
                    target=self.searcher, args=(x, index, array, resultado))
                threads.append(thread)

            index = index + arraySize

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        if (len(resultado) > 0):
            return resultado[0]
        else:
            return -1


ArrayMultithreading = ArrayMultithreading()

randNumbers = numpy.random.randint(1, 1000, 100)
randDivider = numpy.random.randint(1, 100)
randNumber = numpy.random.randint(1, 1000)

aux = ArrayMultithreading.parallelSearch(randNumber, randNumbers, randDivider)

print(aux)
print('Divider: ' + str(randDivider) + '\n Number: ' + str(randNumber))
print(randNumbers)
