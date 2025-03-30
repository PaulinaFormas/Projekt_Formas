package zad3;

// Interfejs funkcji
interface IFunc {
    double func(double x);
    double max(double a, double b);
}

// Pierwsza konkretna funkcja do całkowania
class Funkcja1 implements IFunc {
    @Override
    public double func(double x) {
        return 3 / x;
    }

    @Override
    public double max(double a, double b) {
        return Math.max(a, b);
    }
}

// Druga konkretna funkcja do całkowania
class Funkcja2 implements IFunc {
    @Override
    public double func(double x) {
        // Przykładowe wyrażenie funkcji - tutaj używam funkcji kwadratowej x^2
        return x * x;
    }

    @Override
    public double max(double a, double b) {
        return Math.max(a, b);
    }
}

// Definicja klasy do obliczania całki
class Calka {
    public double calculate(double a, double b, IFunc f, int rep) {
        double dx = (b - a) / rep;
        double sum = 0;
        for (int i = 0; i < rep; i++) {
            sum += f.func(a + i * dx) * dx;
        }
        return sum;
    }
}

// Klasa testowa
class Main {
    public static void main(String[] args) {
        Calka calka = new Calka();
        IFunc funkcja1 = new Funkcja1();
        IFunc funkcja2 = new Funkcja2();

        double a = 1;
        double b = Math.E;
        int rep = 1000; // Liczba podziałów
        int rep1 = 10000;
        int rep2 = 100000;


        // Obliczenia dla Funkcja1
        double wynikCalki1 = calka.calculate(a, b, funkcja1, rep);
        System.out.println("Wynik całki dla 1000 Funkcja1: " + wynikCalki1);

        double wynikCalki2 = calka.calculate(a, b, funkcja1, rep1);
        System.out.println("Wynik całki dla 10000 Funkcja1: " + wynikCalki2);

        double wynikCalki3 = calka.calculate(a, b, funkcja1, rep2);
        System.out.println("Wynik całki dla 100000 Funkcja1: " + wynikCalki3);

        // Teoretyczna wartość całki dla f(x) = 3/x w przedziale [1, e]
        double teoretycznaWartoscCalki1 = 3 * (Math.log(Math.abs(b)) - Math.log(Math.abs(a)));
        System.out.println("Teoretyczna wartość całki dla Funkcja1: " + teoretycznaWartoscCalki1);

        // Obliczenie i wyświetlenie błędu względnego dla Funkcja1
        double bladWzgledny1 = Math.abs((wynikCalki1 - teoretycznaWartoscCalki1) / teoretycznaWartoscCalki1);
        System.out.println("Błąd względny dla Funkcja1: " + bladWzgledny1);

        // Obliczenia dla Funkcja2
        double wynikCalki4 = calka.calculate(a, b, funkcja2, rep);
        System.out.println("Wynik całki dla Funkcja2: " + wynikCalki4);

        // Teoretyczna wartość całki dla f(x) = x^2 w przedziale [1, e]
        double teoretycznaWartoscCalki2 = (Math.pow(b, 3) - Math.pow(a, 3)) / 3.0;
        System.out.println("Teoretyczna wartość całki dla Funkcja2: " + teoretycznaWartoscCalki2);

        // Obliczenie i wyświetlenie błędu względnego dla Funkcja2
        double bladWzgledny2 = Math.abs((wynikCalki2 - teoretycznaWartoscCalki2) / teoretycznaWartoscCalki2);
        System.out.println("Błąd względny dla Funkcja2: " + bladWzgledny2);
    }
}

