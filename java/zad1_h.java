import java.util.Scanner;

public class zad1_h {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        double suma = 0;
        for(int i=1; i<=x; i++)
        {
            double y = input.nextDouble();
            if(i%2==0)
                suma -= y;
            else
                suma += y;
        }
        System.out.println(suma);
    }
}
