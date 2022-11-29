import java.util.Scanner;

public class zad2_2b {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        int notak = 0;
        for(int i=0; i<x; i++)
        {
            double y = input.nextDouble();
            if((y%3==0) && (y%5!=0))
                notak++;
        }
        System.out.println(notak);
    }
}
