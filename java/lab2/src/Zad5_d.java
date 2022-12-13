import java.util.Random;

public class Zad5_d {
    public static void main(String[] args) {
        Random r = new Random();
        int x = r.nextInt(100);
        int suma_ujemnych = 0;
        int suma_dodatnich = 0;
        int[] tab = new int[x];
        for(int i=0; i<x; i++) {
            Random a = new Random();
            int liczba = a.nextInt(999 - (-999)) + (-999);
            tab[i] = liczba;
            if(tab[i]<0)
                suma_ujemnych += tab[i];
            else
                suma_dodatnich += tab[i];
        }
        System.out.println("Suma ujemnych: " + suma_ujemnych);
        System.out.println("Suma dodatnich: " + suma_dodatnich);
    }
}
