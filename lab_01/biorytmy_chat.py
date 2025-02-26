import datetime
import math

def calculate_biorhythm(birth_date, today):
    days_lived = (today - birth_date).days
    physical = math.sin(2 * math.pi * days_lived / 23)
    emotional = math.sin(2 * math.pi * days_lived / 28)
    intellectual = math.sin(2 * math.pi * days_lived / 33)
    
    return days_lived, physical, emotional, intellectual

def check_biorhythm(value, name, next_value):
    if value > 0.5:
        print(f"Twój {name} biorytm jest wysoki ({value:.2f})! Świetny dzień!")
    elif value < -0.5:
        print(f"Twój {name} biorytm jest niski ({value:.2f}). Może być ciężko...")
        if next_value > value:
            print("Nie martw się. Jutro będzie lepiej!")

def main():
    name = input("Podaj swoje imię: ")
    year = int(input("Podaj rok urodzenia: "))
    month = int(input("Podaj miesiąc urodzenia: "))
    day = int(input("Podaj dzień urodzenia: "))
    
    birth_date = datetime.date(year, month, day)
    today = datetime.date.today()
    
    print(f"Witaj, {name}!")
    days_lived, physical, emotional, intellectual = calculate_biorhythm(birth_date, today)
    print(f"Dzisiaj jest {days_lived} dzień Twojego życia.")
    
    tomorrow = today + datetime.timedelta(days=1)
    _, next_physical, next_emotional, next_intellectual = calculate_biorhythm(birth_date, tomorrow)
    
    check_biorhythm(physical, "fizyczny", next_physical)
    check_biorhythm(emotional, "emocjonalny", next_emotional)
    check_biorhythm(intellectual, "intelektualny", next_intellectual)

if __name__ == "__main__":
    main()