public class Deposito {
    private int items = 0;
    private int capacidade = 5;
    private boolean podeRetirar = false;
    private boolean podeColocar = true;
    
    public synchronized int retirar() {

        if (!podeRetirar) {
            System.out.println("Consumidor esperando para retirar...\n");
            try {
                wait();
            } catch(InterruptedException e) {
                System.out.println("Interrompido");
            }
        }

        if (items > 0) {

            items--;
            System.out.println("Caixa retirada: Sobram "+items+" caixas");

            podeColocar = true;

        }

        if (items == 0) {
            podeRetirar = false;
        }

        System.out.println("Consumidor terminou de retirar.\npodeRetirar = "+podeRetirar+"; podeColocar = "+podeColocar+'\n');

        notify();
        return 0;

    }

    public synchronized int colocar () {

        if (!podeColocar) {
            System.out.println("Produtor esperando para colocar...\n");
            try {
                wait();
            } catch(InterruptedException e) {
                System.out.println("Interrompido");
            }
        }

        if (items < capacidade) {

            items++;
            System.out.println("Caixa armazenada: Passaram a ser "+items+" caixas");

            podeRetirar = true;

        }

        if (items == capacidade) {
            podeColocar = false;
        }

        System.out.println("Produtor terminou de colocar.\npodeRetirar = "+podeRetirar+"; podeColocar = "+podeColocar+'\n');

        notify();
        return 0;

    }

    public static void main(String[] args) {

        Deposito dep = new Deposito();
        Produtor prod = new Produtor(dep, 2);
        Consumidor cons = new Consumidor(dep, 1);
        Produtor prod1 = new Produtor(dep, 1);
        Consumidor cons1 = new Consumidor(dep, 5);

        prod.start();
        cons.start();
        prod1.start();
        cons1.start();

    }

}