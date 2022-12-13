import java.util.Random;

public class Zad2_b {
    public static void main(String[] args) {
        Random r = new Random();
        int x = r.nextInt(100);
        int ujemne = 0;
        int dodatnie = 0;
        int zerowe = 0;
        int[] tab = new int[x];
        for(int i=0; i<x; i++){
            Random a = new Random();
            int liczba = a.nextInt(999 -(-999)) + (-999);
            tab[i] = liczba;
            if(tab[i]<0)
                ujemne++;
            if(tab[i]>0)
                dodatnie++;
            if(tab[i]==0)
                zerowe++;
        }
        System.out.println("Ilosc liczb: " + x);
        System.out.println("Ujemne: " + ujemne);
        System.out.println("Dodatnie: " + dodatnie);
        System.out.println("Zerowe: " + zerowe);
    }
}
