import java.util.Scanner;

public class zad2_2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        int nieparzyste = 0;
        for(int i=0; i<x; i++)
        {
            double y = input.nextDouble();
            if(y%2!=0)
                nieparzyste++;
        }
        System.out.println(nieparzyste);
    }
}
