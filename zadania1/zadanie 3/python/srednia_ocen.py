# Średnia ocen w Pythonie
print("Średnia ocen ucznia")
n = int(input("Podaj liczbę ocen: "))
oceny = []

for i in range(n):
    ocena = float(input(f"Podaj ocenę {i+1}: "))
    if ocena < 1 or ocena > 6:
        print("Ocena musi być w skali 1-6!")
        exit()
    oceny.append(ocena)

srednia = sum(oceny) / n
print(f"Średnia: {srednia:.2f}")

if srednia >= 3.0:
    print("Uczeń zdał.")
else:
    print("Uczeń nie zdał.")