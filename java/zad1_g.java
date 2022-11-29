import java.util.Scanner;

public class zad1_g {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        double suma = 0;
        double iloczyn = 1;
        for(int i=0; i<x; i++)
        {
            double y = input.nextDouble();
            suma += y;
            iloczyn *= y;
        }
        System.out.println(suma);
        System.out.println(iloczyn);
    }
}
