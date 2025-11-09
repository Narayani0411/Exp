import random
import numpy as np
import matplotlib.pyplot as plt

# Fitness function
def fitness(x):
    return x * np.sin(10 * np.pi * x) + 1.0

# ---- User Inputs ----
pop_size = int(input("Enter population size: "))
generations = int(input("Enter number of generations: "))
lower = float(input("Enter lower bound: "))
upper = float(input("Enter upper bound: "))

# ---- Initial Population ----
population = [random.uniform(lower, upper) for _ in range(pop_size)]

# ---- Genetic Algorithm ----
for gen in range(generations):
    fitnesses = [max(fitness(x), 1e-8) for x in population]

    best = max(population, key=fitness)
    print(f"Generation {gen+1} → Best x = {best:.4f}, f(x) = {fitness(best):.4f}")

    new_pop = []
    for _ in range(pop_size):
        # selection
        p1, p2 = random.choices(population, weights=fitnesses, k=2)

        # crossover
        child = (p1 + p2) / 2  

        # mutation
        if random.random() < 0.1:
            child += random.uniform(-0.1, 0.1)

        # boundary check
        child = max(min(child, upper), lower)
        new_pop.append(child)

    population = new_pop

# ---- Final Best ----
best = max(population, key=fitness)
print("\n===== FINAL RESULT =====")
print("Best x:", best)
print("Best f(x):", fitness(best))

# ---- Plot Function & Mark Best ----
x_vals = np.linspace(lower, upper, 500)
y_vals = fitness(x_vals)

plt.plot(x_vals, y_vals, label="Fitness Function")
plt.scatter(best, fitness(best), s=80, color="red", label="Best x")  # mark best x
plt.title("Genetic Algorithm Optimization")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()