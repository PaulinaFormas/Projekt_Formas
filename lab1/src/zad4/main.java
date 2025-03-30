package zad4;

import java.util.Random;

class PocztaSimulator {

    private double simTime = 0; // Symulacyjny czas systemowy
    private double[] okienka; // Czasy zajętości poszczególnych okienek
    private int obsluzeniKlienci = 0;

    public PocztaSimulator(int liczbaOkienek) {
        okienka = new double[liczbaOkienek];
        for (int i = 0; i < liczbaOkienek; i++) {
            okienka[i] = 0;
        }
    }

    private Random rand = new Random();
    public void symuluj(double czasZakon, int liczInteresantow) {
        double[] kolejka = new double[liczInteresantow];
        int index = 0;

        while (simTime < czasZakon && obsluzeniKlienci < liczInteresantow) {
            double czasPrzybycia = generujCzasPrzybycia();
            double czasObslugi = generujCzasObslugi();

            System.out.println("Klient przybył o czasie: " + czasPrzybycia);
            kolejka[index++] = czasPrzybycia;

            // Przetwarzanie kolejki klientów
            for (int i = 0; i < index; i++) {
                if (kolejka[i] <= simTime) {
                    System.out.println("Rozpoczynam obsługę klienta, który przybył o czasie: " + kolejka[i]);
                    int okienko = znajdzWolneOkienko();
                    if (okienko != -1) {
                        okienka[okienko] = simTime + czasObslugi;
                        System.out.println("Klient obsłużony w okienku: " + okienko);
                        obsluzeniKlienci++;
                        // Usuwamy obsłużonego klienta z kolejki
                        for (int j = i; j < index - 1; j++) {
                            kolejka[j] = kolejka[j + 1];
                        }
                        index--;
                        i--; // Zmniejszamy i, aby ponownie sprawdzić ten indeks
                    } else {
                        System.out.println("Brak wolnych okienek, klient musi poczekać.");
                    }
                }
            }

            // Aktualizacja czasu symulacji
            simTime++;
        }

        // Podsumowanie stanu okienek na koniec symulacji
        for (int i = 0; i < okienka.length; i++) {
            System.out.println("Okienko " + i + (okienka[i] > simTime ? " jest zajęte do " + okienka[i] : " jest wolne"));
        }
    }

    // funkcje
    private double generujCzasPrzybycia() {
        // przykładowy średni czas między przybyciami klientów (np. 10 minut)
        double lambda = 1.0 / 10.0;
        return -Math.log(1 - rand.nextDouble()) / lambda;
    }

    private double generujCzasObslugi() {
        // przykładowy średni czas obsługi klienta (np. 8 minut)
        double mi = 1.0 / 3.0;
        return -Math.log(1 - rand.nextDouble()) / mi;
    }

    private int znajdzWolneOkienko() {
        for (int i = 0; i < okienka.length; i++) {
            if (simTime >= okienka[i]) {
                return i;
            }
        }
        return -1;
    }


    public static void main(String[] args) {
        int liczbaOkienek = 5; // Załóżmy, że mamy 5 okienek
        double czasZakon = 8 * 60; // Symulacja przez 8 godzin pracy
        int liczInteresantow = 100; // Maksymalna liczba klientów do obsłużenia

        PocztaSimulator simulator = new PocztaSimulator(liczbaOkienek);
        simulator.symuluj(czasZakon, liczInteresantow);

        System.out.println("Obsłużonych klientów: " + simulator.obsluzeniKlienci);
    }
}
