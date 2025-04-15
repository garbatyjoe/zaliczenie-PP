// Kalkulator w C#
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Kalkulator");
        Console.Write("Podaj pierwszą liczbę: ");
        double a = Convert.ToDouble(Console.ReadLine());
        Console.Write("Podaj drugą liczbę: ");
        double b = Convert.ToDouble(Console.ReadLine());
        Console.Write("Wybierz operację (+, -, *, /): ");
        char op = Convert.ToChar(Console.ReadLine());

        double wynik = 0;
        if (op == '+')
            wynik = a + b;
        else if (op == '-')
            wynik = a - b;
        else if (op == '*')
            wynik = a * b;
        else if (op == '/')
        {
            if (b == 0)
            {
                Console.WriteLine("Nie można dzielić przez zero!");
                return;
            }
            wynik = a / b;
        }
        else
        {
            Console.WriteLine("Nieznana operacja!");
            return;
        }

        Console.WriteLine($"Wynik: {wynik}");
    }
}