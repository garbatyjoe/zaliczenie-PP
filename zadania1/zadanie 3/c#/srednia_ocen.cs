// Średnia ocen w C#
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Średnia ocen ucznia");
        Console.Write("Podaj liczbę ocen: ");
        int n = Convert.ToInt32(Console.ReadLine());
        double[] oceny = new double[n];

        for (int i = 0; i < n; i++)
        {
            Console.Write($"Podaj ocenę {i + 1}: ");
            oceny[i] = Convert.ToDouble(Console.ReadLine());
            if (oceny[i] < 1 || oceny[i] > 6)
            {
                Console.WriteLine("Ocena musi być w skali 1-6!");
                return;
            }
        }

        double suma = 0;
        foreach (double ocena in oceny)
            suma += ocena;
        double srednia = suma / n;

        Console.WriteLine($"Średnia: {srednia:F2}");

        if (srednia >= 3.0)
            Console.WriteLine("Uczeń zdał.");
        else
            Console.WriteLine("Uczeń nie zdał.");
    }
}