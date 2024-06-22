import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Введите число:");
        int inputNumber = scanner.nextInt();

        int lowerNumber = (int) Math.sqrt(inputNumber);
        int higherNumber = lowerNumber + 1;

        int lowerSquare = lowerNumber * lowerNumber;
        int higherSquare = higherNumber * higherNumber;

        int diffLower = inputNumber - lowerSquare;
        int diffHigher = higherSquare - inputNumber;

        if (diffLower < diffHigher) {
            System.out.println("Число, квадрат которого ближе всего: " + lowerSquare);
        } else {
            System.out.println("Число, квадрат которого ближе всего: " + higherSquare);
        }
    }
}
