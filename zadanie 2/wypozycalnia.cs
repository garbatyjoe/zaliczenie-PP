using System;
using System.Collections.Generic;

namespace Wypozyczalnia
{
    public class Car
    {
        public int CarId { get; set; }
        public string Brand { get; set; }
        public string Model { get; set; }
        public string CarType { get; set; }
        public decimal DailyPrice { get; set; }
        public bool IsAvailable { get; set; } = true;

        public override string ToString() => $"{Brand} {Model} ({CarType}) - {DailyPrice} PLN/dzień";
    }

    public class Customer
    {
        public int CustomerId { get; set; }
        public string Name { get; set; }
        public string Email { get; set; }

        public override string ToString() => $"{Name} ({Email})";
    }

    public class Rental
    {
        public List<RentalInfo> Rentals { get; } = new List<RentalInfo>();

        public class RentalInfo
        {
            public Car Car { get; set; }
            public Customer Customer { get; set; }
            public int Days { get; set; }
            public decimal TotalCost { get; set; }
        }

        public RentalInfo RentCar(Car car, Customer customer, int days)
        {
            if (!car.IsAvailable)
            {
                Console.WriteLine($"Auto {car.Brand} {car.Model} jest już wynajęte!");
                return null;
            }

            var rentalInfo = new RentalInfo
            {
                Car = car,
                Customer = customer,
                Days = days,
                TotalCost = car.DailyPrice * days
            };

            Rentals.Add(rentalInfo);
            car.IsAvailable = false;

            Console.WriteLine($"Wynajęto: {car} dla {customer} na {days} dni. Koszt: {rentalInfo.TotalCost} PLN");
            return rentalInfo;
        }
    }

    class Program
    {
        static void Main()
        {
            var car1 = new Car { CarId = 1, Brand = "Toyota", Model = "Corolla", CarType = "Sedan", DailyPrice = 150 };
            var customer1 = new Customer { CustomerId = 1, Name = "Jan Kowalski", Email = "jan@example.com" };
            var rentalSystem = new Rental();
            rentalSystem.RentCar(car1, customer1, 5);
        }
    }
}