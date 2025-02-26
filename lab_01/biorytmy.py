from datetime import date
import math

name = input("Podaj imię: ")
year = input("Podaj rok urodzenia: ")
month = input("Podaj miesiąc urodzenia: ")
day = input("Podaj dzień urodzenia: ")

date_of_birth = date(int(year), int(month), int(day))
today = date.today()
days_passed = (today - date_of_birth).days

print(f"Witaj {name}! Dzisiaj mija {days_passed} dzień twojego życia.")

physical_wave = math.sin((2 * math.pi / 23)* days_passed)
print(f"Fala fizyczna: {physical_wave}")
if physical_wave > 0.5: print("Gratuluję dobrego wyniku!")
if physical_wave < -0.5:
    print("Współczuję")
    tomorrow = math.sin((2 * math.pi / 23)* (days_passed + 1))
    if tomorrow > physical_wave: print("Nie martw się, jutro będzie lepiej...")
emotional_wave = math.sin((2 * math.pi / 28)* days_passed)
print(f"Fala emocjonalna: {emotional_wave}")
if emotional_wave > 0.5: print("Gratuluję dobrego wyniku!")
if emotional_wave < -0.5:
    print("Współczuję")
    tomorrow = math.sin((2 * math.pi / 28)* (days_passed + 1))
    if tomorrow > emotional_wave: print("Nie martw się, jutro będzie lepiej...")
intelectual_wave = math.sin((2 * math.pi / 33)* days_passed)
print(f"Fala intelektualna: {intelectual_wave}")
if intelectual_wave > 0.5: print("Gratuluję dobrego wyniku!")
if intelectual_wave < -0.5:
    print("Współczuję")
    tomorrow = math.sin((2 * math.pi / 33)* (days_passed + 1))
    if tomorrow > intelectual_wave: print("Nie martw się, jutro będzie lepiej...")

# Pisałem program około pół godziny