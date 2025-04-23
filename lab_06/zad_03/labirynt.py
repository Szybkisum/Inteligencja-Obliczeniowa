import pygad
import numpy as np
from time import time

L = [[0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
     [1, 1, 0, 0, 0, 1, 0, 1, 1, 0],
     [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
     [0, 1, 0, 1, 1, 0, 0, 1, 1, 0],
     [0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
     [0, 1, 0, 0, 1, 1, 0, 1, 0, 0],
     [0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
     [0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]

x_exit = 9
y_exit = 9

gene_space = [0, 1, 2, 3]

def fitness_func(GA, solution, solutionidx):
    x_end = 0
    y_end = 0
    for i in range(len(solution)):
        match solution[i]:
            case 0:
                new_x = x_end - 1
                if new_x < 0 or L[y_end][new_x] != 0:
                    return (x_end - x_exit) + (y_end - y_exit)
                else:
                    x_end = new_x
            case 1:
                new_y = y_end - 1
                if new_y < 0 or L[new_y][x_end] != 0:
                    return (x_end - x_exit) + (y_end - y_exit)
                else:
                    y_end = new_y
            case 2:
                new_x = x_end + 1
                if new_x > 9 or L[y_end][new_x] != 0:
                    return (x_end - x_exit) + (y_end - y_exit)
                else:
                    x_end = new_x
            case 3:
                new_y = y_end + 1
                if new_y > 9 or L[new_y][x_end] != 0:
                    return (x_end - x_exit) + (y_end - y_exit)
                else:
                    y_end = new_y
                
    return (x_end - x_exit) + (y_end - y_exit)

sol_per_pop = 200
num_genes = 30

num_parents_mating = 100
num_generations = 100
keep_parents = int(0.2 * sol_per_pop)
parent_selection_type = "sss"
crossover_type = "two_points"
mutation_type = "random"
mutation_percent_genes = 4

stop_criteria = "reach_0"

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
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

ga_instance.plot_fitness(save_dir="labirynth")

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

    end = time()
    total_time += end - start

print(f"Średni czas: {total_time/10}s")