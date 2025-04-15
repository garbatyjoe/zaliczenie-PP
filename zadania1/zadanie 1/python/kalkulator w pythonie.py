# Kalkulator w Pythonie
print("Kalkulator")
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
op = input("Wybierz operację (+, -, *, /): ")

if op == '+':
    wynik = a + b
elif op == '-':
    wynik = a - b
elif op == '*':
    wynik = a * b
elif op == '/':
    if b == 0:
        print("Nie można dzielić przez zero!")
        exit()
    wynik = a / b
else:
    print("Nieznana operacja!")
    exit()

print(f"Wynik: {wynik}")