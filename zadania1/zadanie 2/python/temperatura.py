# Konwerter temperatur w Pythonie
print("Konwerter temperatur (C ↔ F)")
wybor = input("Wybierz kierunek konwersji (C → F wpisz 'C', F → C wpisz 'F'): ").upper()

if wybor == 'C':
    celsius = float(input("Podaj temperaturę w °C: "))
    fahrenheit = celsius * 1.8 + 32
    print(f"{celsius}°C = {fahrenheit}°F")
elif wybor == 'F':
    fahrenheit = float(input("Podaj temperaturę w °F: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit}°F = {celsius}°C")
else:
    print("Nieprawidłowy wybór!")