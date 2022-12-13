import java.util.Random;

public class Zad3_c {
    public static void main(String[] args) {
        Random r = new Random();
        int x = r.nextInt(100);
        int[] tab = new int[x];
        int maks = tab[0];
        int ile = 0;
        for(int i=1; i<x; i++){
            Random a = new Random();
            int liczba = a.nextInt(999 -(-999)) + (-999);
            tab[i] = liczba;
            if(tab[i]>maks)
                maks = tab[i];
        }
        for(int i=1; i<x; i++){
            if(tab[i] == maks)
                ile++;
        }
        System.out.println("Najwiekszy element: " + maks);
        System.out.println("Wystapil: " + ile + " razy");
    }
}
