import pygad
import numpy as np
import math

def endurance(x, y, z, u, v, w):
    return math.exp(-2*(y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w)

gene_space = {"low": 0, "high": 1}

def fitness_func(GA, solution, solutionidx):
    return endurance(*solution)

sol_per_pop = 10
num_genes = 6

num_parents_mating = 5
num_generations = 50
keep_parents = int(0.2 * sol_per_pop)
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 20

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
)

ga_instance.run()
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
prediction = endurance(*solution)
print("Predicted output based on the best solution :{prediction}".format(prediction=prediction))

ga_instance.plot_fitness(save_dir="endurance")

# [0.73876029 0.69243813 0.99879597 0.99970066 0.34961564 0.00145614]
# 2.8399310521444088