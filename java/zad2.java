import java.util.Scanner;

public class zad2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        double[] tablica;
        tablica = new double[x];
        for(int i=0; i<x; i++)
        {
            double y = input.nextDouble();
            tablica[i] = y;
        }
        for(int i=1; i<x; i++)
        {
            System.out.println(tablica[i]);
        }
        System.out.println(tablica[0]);
    }
}
