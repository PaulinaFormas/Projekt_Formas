package zad2;

import java.util.Random;

class MyRandom {
    private Random random;
    private long a;
    private long b;
    private long M;
    private long xn; // aktualny stan generatora

    public MyRandom(long a, long b, long M, long seed) {
        this.random = new Random(seed);
        this.a = a;
        this.b = b;
        this.M = M;
        this.xn = seed;
    }

    public int nextInt() {
        xn = (a * xn + b) % M;
        return (int) xn;
    }

    public double nextDouble() {
        return ((double)nextInt()) / M;
    }

    // Nowa metoda generująca
    public int discrete(double[] xx, double[] p) {
        double r = nextDouble();
        double sum = 0.0;
        for (int i = 0; i < p.length; i++) {
            sum += p[i];
            if (r < sum) {
                return (int) xx[i];
            }
        }
        return (int) xx[xx.length - 1]; // w przypadku gdyby r było bliskie 1
    }

    // Metoda główna
    public static void main(String[] args) {
        long a = 23;
        long b = 11;
        long M = 100;
        long seed = 1;

        MyRandom myRandom = new MyRandom(a, b, M, seed);

        // Zdefiniowanie rozkładu dyskretnego
        double[] xx = {-2, -1, 0, 1, 2, 3, 4};
        double[] p = {0.1, 0.1, 0.2, 0.2, 0.2, 0.1, 0.1};


        // Generowanie próbek i obliczanie średniej
        int samples = 10000;
        double sumOfValues = 0.0;
        for (int i = 0; i < samples; i++) {
            sumOfValues += myRandom.discrete(xx, p);
        }
        double mean = sumOfValues / samples;

        // Obliczanie teoretycznej średniej
        double theoreticalMean = 0.0;
        for (int i = 0; i < xx.length; i++) {
            theoreticalMean += xx[i] * p[i];
        }

        // Wyświetlenie wyników
        System.out.println("Empiryczna średnia: " + mean);
        System.out.println("Teoretyczna średnia: " + theoreticalMean);
        System.out.println("Błąd względny: " + Math.abs(mean - theoreticalMean) / theoreticalMean);
    }
}

