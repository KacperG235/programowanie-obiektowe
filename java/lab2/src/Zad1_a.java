import java.util.Random;

public class Zad1_a {
    public static void main(String[] args) {
        Random r = new Random();
        int x = r.nextInt(100);
        int ilep = 0;
        int ilen = 0;
        int[] tab = new int[x];
        for (int i = 0; i < x; i++) {
            Random a = new Random();
            int liczba = a.nextInt(999 -(-999)) + (-999);
            tab[i] = liczba;
            if(tab[i]%2==0)
                ilep++;
            else
                ilen++;
        }
        System.out.println("Ilosc liczb: " + x);
        System.out.println("Ilosc parzysytch: " + ilep);
        System.out.println("Ilosc nieparzysytch: " + ilen);
    }
}