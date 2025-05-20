class Car:
    def __init__(self, car_id, brand, model, car_type, daily_price):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.car_type = car_type  # np. "SUV", "Sedan", "Sport"
        self.daily_price = daily_price
        self.is_available = True

    def __str__(self):
        return f"{self.brand} {self.model} ({self.car_type}) - {self.daily_price} PLN/dzień"
    
    class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"
    
    class Rental:
    def __init__(self):
        self.rentals = []

    def rent_car(self, car, customer, days):
        if not car.is_available:
            print(f"Auto {car.brand} {car.model} jest już wynajęte!")
            return None
        
        total_cost = car.daily_price * days
        rental_info = {
            "car": car,
            "customer": customer,
            "days": days,
            "total_cost": total_cost
        }
        self.rentals.append(rental_info)
        car.is_available = False
        
        print(f"Wynajęto: {car} dla {customer} na {days} dni. Koszt: {total_cost} PLN")
        return rental_info

if __name__ == "__main__":
    car1 = Car(1, "Toyota", "Corolla", "Sedan", 150)
    customer1 = Customer(1, "Jan Kowalski", "jan@example.com")
    rental_system = Rental()
    rental_system.rent_car(car1, customer1, 5)