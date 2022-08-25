public class TesteContador { 
    public static void main(String args[]) {
        Contador th1 = new Contador("th-1");
        Contador th2 = new Contador("th-2");
        th1.start();
        th2.start();
    }

}

public class Contador extends Thread implements Runnable {
    private String name;
    public Contador(String name) {
        this.name = name;
    }
    public void run() {
        for (int i = 0; i <= 10; i++) {
            System.out.println(this.name + " contando...  " + i);
        }
    }

}