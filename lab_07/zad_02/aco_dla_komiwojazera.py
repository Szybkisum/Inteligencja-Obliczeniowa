import matplotlib.pyplot as plt
import random

from aco import AntColony


plt.style.use("dark_background")


COORDS = (
    (42, 87),
    (13, 59),
    (76, 3),
    (91, 28),
    (65, 65),
    (8, 99),
    (33, 44),
    (50, 12),
    (71, 6),
    (24, 90),
    (20, 52),
    (43, 50),
    (20, 84),
    (70, 65),
    (29, 90),
    (87, 83),
    (73, 23),
)


def random_coord():
    r = random.randint(0, len(COORDS))
    return r


def plot_nodes(w=12, h=8):
    for x, y in COORDS:
        plt.plot(x, y, "g.", markersize=15)
    plt.axis("off")
    fig = plt.gcf()
    fig.set_size_inches([w, h])


def plot_all_edges():
    paths = ((a, b) for a in COORDS for b in COORDS)

    for a, b in paths:
        plt.plot((a[0], b[0]), (a[1], b[1]))

# plot_nodes()
# plot_all_edges()
# plt.savefig("all_edges.png")

configs = [
    # INITIAL TRIES
    # {"ant_count": 300, "alpha": 1.0, "beta": 2.0, "pheromone_evaporation_rate": 0.3, "pheromone_constant": 1000, "iterations": 300},
    # {"ant_count": 300, "alpha": 0.5, "beta": 4.0, "pheromone_evaporation_rate": 0.5, "pheromone_constant": 2000, "iterations": 300}, --> 417
    # {"ant_count": 300, "alpha": 1.5, "beta": 3.0, "pheromone_evaporation_rate": 0.4, "pheromone_constant": 500, "iterations": 300}, --> 417
    # {"ant_count": 300, "alpha": 1.0, "beta": 5.0, "pheromone_evaporation_rate": 0.2, "pheromone_constant": 1000, "iterations": 300},

    # Around config 2
    # {"ant_count": 300, "alpha": 0.3, "beta": 5.0, "pheromone_evaporation_rate": 0.5, "pheromone_constant": 2000, "iterations": 300},
    # {"ant_count": 300, "alpha": 0.5, "beta": 6.0, "pheromone_evaporation_rate": 0.5, "pheromone_constant": 3000, "iterations": 300},
    # {"ant_count": 300, "alpha": 0.7, "beta": 4.0, "pheromone_evaporation_rate": 0.5, "pheromone_constant": 1500, "iterations": 300}, --> 347

    # Around config 3
    # {"ant_count": 300, "alpha": 1.2, "beta": 2.5, "pheromone_evaporation_rate": 0.4, "pheromone_constant": 500, "iterations": 300}, --> 347
    # {"ant_count": 300, "alpha": 1.5, "beta": 3.0, "pheromone_evaporation_rate": 0.4, "pheromone_constant": 1000, "iterations": 300},
    # {"ant_count": 300, "alpha": 1.8, "beta": 3.5, "pheromone_evaporation_rate": 0.4, "pheromone_constant": 500, "iterations": 300},

    # Group A
    # {"ant_count": 300, "alpha": 0.6, "beta": 4.0, "pheromone_evaporation_rate": 0.5, "pheromone_constant": 1500, "iterations": 300},
    # {"ant_count": 300, "alpha": 0.7, "beta": 4.5, "pheromone_evaporation_rate": 0.5, "pheromone_constant": 1500, "iterations": 300},
    # {"ant_count": 300, "alpha": 0.7, "beta": 4.0, "pheromone_evaporation_rate": 0.4, "pheromone_constant": 1500, "iterations": 300},
    # {"ant_count": 300, "alpha": 0.8, "beta": 4.0, "pheromone_evaporation_rate": 0.5, "pheromone_constant": 1500, "iterations": 300}, --> 347
    # {"ant_count": 300, "alpha": 0.7, "beta": 3.8, "pheromone_evaporation_rate": 0.5, "pheromone_constant": 1500, "iterations": 300}, --> 347
    # {"ant_count": 300, "alpha": 0.7, "beta": 4.0, "pheromone_evaporation_rate": 0.5, "pheromone_constant": 1200, "iterations": 300},
    # {"ant_count": 300, "alpha": 0.6, "beta": 4.5, "pheromone_evaporation_rate": 0.5, "pheromone_constant": 1800, "iterations": 300},

    # Group B
    # {"ant_count": 300, "alpha": 1.2, "beta": 2.5, "pheromone_evaporation_rate": 0.4, "pheromone_constant": 750, "iterations": 300},
    # {"ant_count": 300, "alpha": 1.1, "beta": 2.3, "pheromone_evaporation_rate": 0.4, "pheromone_constant": 500, "iterations": 300},
    # {"ant_count": 300, "alpha": 1.3, "beta": 2.7, "pheromone_evaporation_rate": 0.4, "pheromone_constant": 500, "iterations": 300},
    # {"ant_count": 300, "alpha": 1.2, "beta": 2.5, "pheromone_evaporation_rate": 0.35, "pheromone_constant": 500, "iterations": 300},
    # {"ant_count": 300, "alpha": 1.2, "beta": 2.8, "pheromone_evaporation_rate": 0.4, "pheromone_constant": 500, "iterations": 300},
    # {"ant_count": 300, "alpha": 1.0, "beta": 2.5, "pheromone_evaporation_rate": 0.4, "pheromone_constant": 600, "iterations": 300},
    # {"ant_count": 300, "alpha": 1.2, "beta": 2.5, "pheromone_evaporation_rate": 0.4, "pheromone_constant": 400, "iterations": 300},

    # Mixed Region Explorations
    # {"ant_count": 300, "alpha": 1.0, "beta": 3.0, "pheromone_evaporation_rate": 0.4, "pheromone_constant": 1000, "iterations": 300},
    # {"ant_count": 300, "alpha": 0.9, "beta": 3.5, "pheromone_evaporation_rate": 0.45, "pheromone_constant": 1000, "iterations": 300},
    # {"ant_count": 300, "alpha": 1.1, "beta": 3.0, "pheromone_evaporation_rate": 0.4, "pheromone_constant": 1000, "iterations": 300},
    # {"ant_count": 300, "alpha": 0.8, "beta": 3.2, "pheromone_evaporation_rate": 0.4, "pheromone_constant": 800, "iterations": 300},
    # {"ant_count": 300, "alpha": 1.0, "beta": 3.8, "pheromone_evaporation_rate": 0.4, "pheromone_constant": 1000, "iterations": 300},
    # {"ant_count": 300, "alpha": 1.2, "beta": 3.2, "pheromone_evaporation_rate": 0.4, "pheromone_constant": 1000, "iterations": 300},

    {"ant_count": 200, "alpha": 0.75, "beta": 4.0, "pheromone_evaporation_rate": 0.5, "pheromone_constant": 1450, "iterations": 500},
    {"ant_count": 200, "alpha": 0.75, "beta": 4.2, "pheromone_evaporation_rate": 0.5, "pheromone_constant": 1500, "iterations": 500},
    {"ant_count": 200, "alpha": 0.8, "beta": 4.2, "pheromone_evaporation_rate": 0.5, "pheromone_constant": 1450, "iterations": 500},
    {"ant_count": 200, "alpha": 0.7, "beta": 3.9, "pheromone_evaporation_rate": 0.45, "pheromone_constant": 1500, "iterations": 500},
    {"ant_count": 200, "alpha": 0.65, "beta": 4.0, "pheromone_evaporation_rate": 0.5, "pheromone_constant": 1600, "iterations": 500}, # --> 347
    {"ant_count": 200, "alpha": 0.7, "beta": 4.0, "pheromone_evaporation_rate": 0.5, "pheromone_constant": 1400, "iterations": 500}, # --> 347
]

distances = []

for i in range(len(configs)):
    plt.figure()
    plot_nodes()
    colony = AntColony(COORDS, **configs[i])

    distances.append(colony.bestDistance)
    optimal_nodes = colony.get_path()

    for j in range(len(optimal_nodes) - 1):
        plt.plot(
            (optimal_nodes[j][0], optimal_nodes[j + 1][0]),
            (optimal_nodes[j][1], optimal_nodes[j + 1][1]),
        )

    print(optimal_nodes)
    plt.savefig(f"komiwojazer{i + 1}.png")
    plt.close()

for i in range(len(configs)):
    print(i, ": ", configs[i], distances[i])

# 347.2730351784239
# [(65, 65), (70, 65), (87, 83), (42, 87), (29, 90), (24, 90), (20, 84), (8, 99), (13, 59), (20, 52), (33, 44), (43, 50), (50, 12), (71, 6), (76, 3), (73, 23), (91, 28), (65, 65)]