import java.util.Scanner;

public class zad1_d {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        double suma = 1;
        for(int i=0; i<x; i++)
        {
            double y = input.nextDouble();
            suma += Math.sqrt(y);
        }
        System.out.println(suma);
    }
}
