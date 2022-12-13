import java.util.Random;

public class zad1_f {
    public static void main(String[] args) {
        Random r = new Random();
        int x = r.nextInt(100);
        int[] tab = new int[x];
        for(int i=0; i<x; i++){
            Random a = new Random();
            int liczba = a.nextInt(999 - (-999)) + (-999);
            tab[i] = liczba;
            if(tab[i]>0)
                tab[i] = 1;
            if(tab[i]<0)
                tab[i] = -1;
        }
        for(int i=0; i<x; i++)
            System.out.println(tab[i]);
    }
}
