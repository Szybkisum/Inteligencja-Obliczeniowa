import pygad
import numpy as np
from time import time

name = ["zegar", "opraz-pejzaż", "opraz-protret", "radio", "laptop", "lampka nocna", "srebrne sztućce", "porcelana", "figura_z_brązu", "skórzana torebka", "odkurzacz"]
value = [100, 300, 200, 40, 500, 70, 100, 250, 300, 280, 300]
weight = [7, 7, 6, 2, 5, 6, 1, 3, 10, 3, 15]

max_weight = 25
C = 1500

S = [
    {"name": n, "value": v, "weight": w}
    for n, v, w in zip(name, value, weight)
]

gene_space = [0, 1]

def fitness_func(GA, solution, solutionidx):
    weight = 0
    value = 0

    for i in range(len(solution)):
        if solution[i] == 1:
            value += S[i]["value"]
            weight += S[i]["weight"]

    penalty = max(0, weight - max_weight) * C
    fitness = value - penalty
    return fitness

sol_per_pop = 10
num_genes = len(S)

num_parents_mating = 5
num_generations = 30
keep_parents = int(0.2 * sol_per_pop)
parent_selection_type = "sss"
crossover_type = "two_points"
mutation_type = "random"
mutation_percent_genes = 10

stop_criteria = "reach_1630"

ga_instance = pygad.GA(
    gene_space=gene_space,
    fitness_func=fitness_func,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    num_parents_mating=num_parents_mating,
    num_generations=num_generations,
    keep_parents=keep_parents,
    parent_selection_type=parent_selection_type,
    crossover_type=crossover_type,
    mutation_type=mutation_type,
    mutation_percent_genes=mutation_percent_genes,
    # stop_criteria=stop_criteria
)

ga_instance.run()
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

prediction = ""
for i in range(len(solution)):
    if solution[i] == 1:
        prediction += S[i]["name"] + "\n"
print("Predicted output based on the best solution :\n{prediction}".format(prediction=prediction))

ga_instance.plot_fitness(save_dir="bag")

correct = 0
total_time = 0
for i in range(0, 10):
    start = time()

    ga_instance = pygad.GA(
    gene_space=gene_space,
    fitness_func=fitness_func,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    num_parents_mating=num_parents_mating,
    num_generations=num_generations,
    keep_parents=keep_parents,
    parent_selection_type=parent_selection_type,
    crossover_type=crossover_type,
    mutation_type=mutation_type,
    mutation_percent_genes=mutation_percent_genes,
    stop_criteria=stop_criteria
    )

    ga_instance.run()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    if solution_fitness == 1630:
        correct += 1

    end = time()
    total_time += end - start

print(f"Dokładność: {correct/10 * 100}%")
print(f"Średni czas: {total_time/10}s")

# [0. 1. 1. 0. 1. 0. 1. 1. 0. 1. 0.]
# 1630
# opraz-pejzaż
# opraz-protret
# laptop
# srebren sztućce
# porcelana
# skórzana torebka