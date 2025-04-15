// Konwerter temperatur w C#
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Konwerter temperatur (C ↔ F)");
        Console.Write("Wybierz kierunek konwersji (C → F wpisz 'C', F → C wpisz 'F'): ");
        char wybor = Convert.ToChar(Console.ReadLine().ToUpper());

        if (wybor == 'C')
        {
            Console.Write("Podaj temperaturę w °C: ");
            double celsius = Convert.ToDouble(Console.ReadLine());
            double fahrenheit = celsius * 1.8 + 32;
            Console.WriteLine($"{celsius}°C = {fahrenheit}°F");
        }
        else if (wybor == 'F')
        {
            Console.Write("Podaj temperaturę w °F: ");
            double fahrenheit = Convert.ToDouble(Console.ReadLine());
            double celsius = (fahrenheit - 32) / 1.8;
            Console.WriteLine($"{fahrenheit}°F = {celsius}°C");
        }
        else
        {
            Console.WriteLine("Nieprawidłowy wybór!");
        }
    }
}