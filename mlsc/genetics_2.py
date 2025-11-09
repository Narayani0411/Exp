# =====================================================
# Genetic Algorithm Steps (Simple Version)
# Population = {12, 5, 25, 19}
# =====================================================

# 1. ENCODE (convert decimal → binary)
def encode(x):
    return format(x, '05b')   # 5-bit encoding

# 2. DECODE (binary → decimal)
def decode(b):
    return int(b, 2)

# 3. CROSSOVER FUNCTIONS

# (A) Single-Point Crossover
def single_point_crossover(p1, p2):
    point = 2
    c1 = p1[:point] + p2[point:]
    c2 = p2[:point] + p1[point:]
    return c1, c2

# (B) Two-Point Crossover
def two_point_crossover(p1, p2):
    i, j = 1, 4
    c1 = p1[:i] + p2[i:j] + p1[j:]
    c2 = p2[:i] + p1[i:j] + p2[j:]
    return c1, c2

# 4. MUTATION FUNCTIONS

# (A) Bit Flip Mutation
def bit_flip_mutation(b):
    i = 2  # flip bit-3
    b = list(b)
    b[i] = "1" if b[i] == "0" else "0"
    return "".join(b)

# (B) Swap Mutation
def swap_mutation(b):
    i, j = 1, 4  # swap bit-2 and bit-5
    b = list(b)
    b[i], b[j] = b[j], b[i]
    return "".join(b)

# =====================================================
# MAIN PROGRAM
# =====================================================

# Initial population
population = [12, 5, 25, 19]
print("Initial Population:", population)

# Step 1: Encode
encoded = [encode(x) for x in population]
print("\nEncoded Population:", encoded)

# Step 2: Apply Two Crossovers
c1, c2 = single_point_crossover(encoded[0], encoded[2])
c3, c4 = two_point_crossover(encoded[1], encoded[3])
children = [c1, c2, c3, c4]
print("\nAfter Crossovers:", children)

# Step 3: Apply Two Mutations
m1 = bit_flip_mutation(children[0])   # mutate child1
m2 = swap_mutation(children[1])       # mutate child2
m3 = children[2]                      # unchanged
m4 = children[3]                      # unchanged
mutated = [m1, m2, m3, m4]
print("\nAfter Mutations:", mutated)

# Step 4: Decode mutated population
decoded = [decode(b) for b in mutated]
print("\nDecoded Final Population:", decoded)