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