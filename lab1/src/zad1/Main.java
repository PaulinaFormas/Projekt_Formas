package zad1;

import java.util.List;
import java.util.ArrayList;


class MyRandom {
    private long a;
    private long b;
    private long M;
    private long seed;
    private long xn; // aktualny stan generatora

    // Konstruktor parametryczny
    public MyRandom(long a, long b, long M, long seed) {
        this.a = a;
        this.b = b;
        this.M = M;
        this.seed = seed;
        this.xn = seed;
    }

    // Pierwsza metoda [0, M)
    public int nextInt() {
        xn = (a * xn + b) % M;
        return (int) xn;
    }

    // Druga metoda [0, 1)
    public double nextDouble() {
        return ((double)nextInt()) / M;
    }

    // Trzecia metoda [low, high)
    public double nextDouble(double low, double high) {
        if (low >= high) {
            System.out.print("low musi być większa niż high");
        }
        return low + (high - low) * nextDouble();
    }

    // Czwarta metoda, generuje liczby z rozkładu wykładniczego
    public double exponential(double lambda) {
        if (lambda <= 0) {
            System.out.print("Lambda musi być dodatnia");
        }
        return -Math.log(1 - nextDouble()) / lambda;  //-[ln(1-u)]/lambda
    }

    // Metoda do obliczenia średniej
    public double calculateMean(int samples, String methodName) {
        double sum = 0.0;
        for (int i = 0; i < samples; i++) {
            switch (methodName) {
                case "nextInt":
                    sum += nextInt();
                    break;
                case "nextDouble":
                    sum += nextDouble();
                    break;
                case "nextDoubleRange":
                    sum += nextDouble(0, 1); // Dla demonstracji używam zakresu [0, 1)
                    break;
                case "exponential":
                    sum += exponential(1); // Dla demonstracji lambda ustawiona na 1
                    break;
                default:
                    System.out.print("blad");
            }
        }
        return sum / samples;
    }

    // Główna metoda do uruchomienia programu
    public static void main(String[] args) {
        long a = 23;
        long b = 11;
        long M = 100; // Zakładając, że M = 100 dla przykładu
        long seed = 1; // Ziarno początkowe

        MyRandom myRandom = new MyRandom(a, b, M, seed);

        int samples = 1000; // Ilość generowanych wartości do obliczenia średniej
        double meanInt = myRandom.calculateMean(samples, "nextInt");
        double meanDouble = myRandom.calculateMean(samples, "nextDouble");
        double meanDoubleRange = myRandom.calculateMean(samples, "nextDoubleRange");
        double meanExponential = myRandom.calculateMean(samples, "exponential");

        // Wypisanie średnich i obliczenie błędu względnego
        System.out.println("Średnia nextInt: " + meanInt);
        System.out.println("Błąd względny nextInt: " + Math.abs(meanInt - (M - 1) / 2.0) / ((M - 1) / 2.0));
        System.out.println("Średnia nextDouble: " + meanDouble);
        System.out.println("Błąd względny nextDouble: " + Math.abs(meanDouble - 0.5) / 0.5);
        System.out.println("Średnia nextDoubleRange: " + meanDoubleRange);
        System.out.println("Błąd względny nextDoubleRange: " + Math.abs(meanDoubleRange - 0.5) / 0.5);
        System.out.println("Średnia exponential: " + meanExponential);
        System.out.println("Błąd względny exponential: " + Math.abs(meanExponential - 1) / 1);
    }
}


