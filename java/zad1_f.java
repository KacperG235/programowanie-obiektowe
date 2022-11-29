import java.util.Scanner;

public class zad1_f {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        double suma = 0;
        for(int i=0; i<x; i++)
        {
            double y = input.nextDouble();
            suma += Math.pow(y, 2);
        }
        System.out.println(suma);
    }
}
