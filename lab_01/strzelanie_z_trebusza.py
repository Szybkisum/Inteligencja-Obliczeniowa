import math
import matplotlib.pyplot as plt
import numpy as np

h = 100
v_0 = 50
g = 9.81

def calculate_distance(alpha):
    alpha_rad = math.radians(alpha)
    
    # Obliczanie składowych prędkości
    cos_alpha = math.cos(alpha_rad)
    sin_alpha = math.sin(alpha_rad)
    
    # Obliczanie wyrażenia pod pierwiastkiem
    term = math.sqrt((v_0 * sin_alpha)**2 + 2 * g * h)
    
    # Obliczanie zasięgu
    distance = (v_0 * cos_alpha) / g * (v_0 * sin_alpha + term)
    return distance

def save_projectile_motion(alpha):
    alpha_rad = math.radians(alpha)

    t_flight = (v_0 * math.sin(alpha_rad) + math.sqrt((v_0 * math.sin(alpha_rad))**2 + 2 * g * h)) / g

    t = np.linspace(0, t_flight, num=500)

    x = v_0 * math.cos(alpha_rad) * t
    y = h + v_0 * math.sin(alpha_rad) * t - 0.5 * g * t**2

    plt.figure(figsize=(10, 5))
    plt.plot(x, y)
    plt.grid()
    plt.title("Projectile Motion for the Trebuchet")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.savefig("trajektoria.png")

target = int(input("Podaj punkt w jaki celujesz (liczba całkowita z przedziału [50, 340]): "))

num_o_trys = 0
while True:
    alpha = int(input("Podaj kąt celowania trebusza w stopniach: "))
    num_o_trys += 1
    distance = calculate_distance(alpha)
    print(f"Pocisk spadł w odległości {distance}m od trebusza")
    if distance >= (target - 5) and distance <= (target + 5):
        if num_o_trys == 1:
            print("Cel trafiony za pierwszym razem!")
        else:
            print(f"Cel trafiony w {num_o_trys} próbach!")
        break
    else:
        print("Nie trafiono celu!\nSpróbuj ponownie")

save_projectile_motion(alpha)
