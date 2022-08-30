import time
import random
import threading

lebreGanhadora = None
classificacao = []


class lebre(threading.Thread):
    def __init__(self, idLebre, nome):
        threading.Thread.__init__(self)
        self.idLebre = idLebre
        self.nome = nome
        self.qtdSaltos = 0
        self.distanciaPercorida = 0

    def run(self):

        global lebreGanhadora

        while self.distanciaPercorida < 20:

            distanciaSalto = random.randint(1, 3)

            self.distanciaPercorida = self.distanciaPercorida + distanciaSalto
            self.qtdSaltos = self.qtdSaltos + 1

            print(self.nome+' saltou '+str(distanciaSalto)+' metros')

            if (self.distanciaPercorida >= 20 and lebreGanhadora == None):
                lebreGanhadora = self.idLebre

            time.sleep(0.0001)

        if (self.distanciaPercorida >= 20):
            classificacao.append(self.idLebre)


lebres = []

for i in range(5):
    nomeLebre = 'Lebre-'+str(i+1)
    l = lebre(i, nomeLebre)
    lebres.append(l)

for l in lebres:
    l.start()

for l in lebres:
    l.join()

if (lebreGanhadora != None):
    print('lebreGanhadora: '+lebres[lebreGanhadora].nome)

    for i, idLebre in enumerate(classificacao):
        lebre = lebres[idLebre]
        print(str(i+1)+'º lugar: '+lebre.nome +
              ' - '+str(lebre.qtdSaltos)+' saltos')
