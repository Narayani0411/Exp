# Q1. Genetic Algorithm with initial population = {12, 5, 25, 19}

# -----------------------------------------
# 1. Evaluate Solution (Fitness Function)
# -----------------------------------------

def fitness(x):
    return x * x   # example: f(x) = x^2

population = [12, 5, 25, 19]

print("Initial Population:", population)
print("\n1. Fitness of each solution:")
for x in population:
    print(f"x = {x}, fitness = {fitness(x)}")


# -----------------------------------------
# 2. Define Two Crossover Functions
# -----------------------------------------

# Single-Point Crossover
def single_point_crossover(p1, p2):
    point = 1  # crossover after index 1
    child1 = p1[:point] + p2[point:]
    child2 = p2[:point] + p1[point:]
    return child1, child2

# Two-Point Crossover
def two_point_crossover(p1, p2):
    p1_cut, p2_cut = 1, 3
    child1 = p1[:p1_cut] + p2[p1_cut:p2_cut] + p1[p2_cut:]
    child2 = p2[:p1_cut] + p1[p1_cut:p2_cut] + p2[p2_cut:]
    return child1, child2

print("\n2. Defined Crossover Functions:")
print("→ single_point_crossover(p1, p2)")
print("→ two_point_crossover(p1, p2)")


# -----------------------------------------
# 3. Define Two Mutation Functions
# -----------------------------------------

# Bit Flip Mutation (for binary strings)
def bit_flip_mutation(b):
    i = 0  # flip first bit for example
    b = list(b)
    b[i] = '1' if b[i] == '0' else '0'
    return "".join(b)

# Swap Mutation (swap two positions)
def swap_mutation(b):
    i, j = 1, 3
    b = list(b)
    b[i], b[j] = b[j], b[i]
    return "".join(b)

print("\n3. Defined Mutation Functions:")
print("→ bit_flip_mutation(binary_string)")
print("→ swap_mutation(binary_string)")