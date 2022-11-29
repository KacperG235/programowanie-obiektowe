import java.util.Scanner;
import java.lang.Math;
public class zad1_2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        double iloczyn = 1;
        for(int i=0; i<x; i++)
        {
            double y = input.nextDouble();
            iloczyn = iloczyn * y;
        }
        System.out.println(iloczyn);
    }
}
