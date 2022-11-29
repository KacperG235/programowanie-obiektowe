import java.util.Scanner;

public class zad1_i {

    public static int factorial(int n){
        int fact = 1;
        for(int i=2; i<=n; i++)
        {
            fact *= i;
        }
        return fact;
    }
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        double suma = 0;
        for(int i=1; i<=x; i++)
        {
            double y = input.nextDouble();
            if(i%2!=0)
                suma -= y/factorial(i);
            else
                suma += y/factorial(i);
        }
        System.out.println(suma);
    }
}
