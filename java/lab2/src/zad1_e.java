import java.util.Random;

public class zad1_e {
    public static void main(String[] args) {
        Random r = new Random();
        int x = r.nextInt(100);
        int[] tab = new int[x];
        int dl = 0;
        int naj = 0;
        for (int i = 0; i < x; i++) {
            Random a = new Random();
            int liczba = a.nextInt(999 - (-999)) + (-999);
            tab[i] = liczba;
            if(tab[i]>0)
                dl++;
            else {
                if(dl>naj)
                    naj = dl;
                dl = 0;
            }
        }
        for (int i = 0; i < x; i++)
            System.out.println(tab[i]);
        System.out.println("Najdluzszy dodatnik fragement tablicy: " + naj);
    }
}
