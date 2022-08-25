public class Produtor extends Thread implements Runnable {

    private Deposito dep;
    private int tempo;

    public Produtor(Deposito d, int t){
        this.dep = d;
        this.tempo = t;
    }

    public void run() {

        while (true) {

            try {
                Thread.sleep(tempo*1000);
            } catch(InterruptedException e) {
                System.out.println("Interrompido");
            }

            dep.colocar();

        }

    }

}