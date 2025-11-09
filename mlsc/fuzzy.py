import numpy as np
import matplotlib.pyplot as plt


A = np.array([[0.2, 0.5, 0.7, 1.0],
              [0.4, 0.6, 0.3, 0.9]])

B = np.array([[0.3, 0.7, 0.5, 0.8],
              [0.1, 0.4, 0.6, 0.2]])



union = np.fmax(A, B)
intersection = np.fmin(A, B)
complement_A = 1 - A
complement_B = 1 - B
algebraic_sum = A + B - (A * B)
algebraic_product = A * B
bounded_sum = np.minimum(1, A + B)
bounded_difference = np.maximum(0, A + B - 1)


print("A:\n", A)
print("\nB:\n", B)
print("\nUnion:\n", union)
print("\nIntersection:\n", intersection)
print("\nAlgebraic Sum:\n", algebraic_sum)
print("\nAlgebraic Product:\n", algebraic_product)
print("\nBounded Sum:\n", bounded_sum)
print("\nBounded Difference:\n", bounded_difference)


elements = np.arange(A.shape[1])


plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plt.plot(elements, A[0], 'bo-', label='A₁')
plt.plot(elements, B[0], 'ro-', label='B₁')
plt.plot(elements, union[0], 'g--', label='Union (A₁ ∪ B₁)')
plt.plot(elements, intersection[0], 'm--', label='Intersection (A₁ ∩ B₁)')
plt.plot(elements, algebraic_sum[0], 'y--', label='Algebraic Sum')
plt.plot(elements, algebraic_product[0], 'k--', label='Algebraic Product')
plt.plot(elements, bounded_sum[0], 'b:', label='Bounded Sum')
plt.plot(elements, bounded_difference[0], 'r:', label='Bounded Difference')
plt.title("Fuzzy Set Operations Visualization (Set 1)", fontsize=13)
plt.xlabel("Elements")
plt.ylabel("Membership Value")
plt.ylim(0, 1.1)
plt.legend()
plt.grid(True)


plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 2)
plt.plot(elements, A[1], 'bo-', label='A₂')
plt.plot(elements, B[1], 'ro-', label='B₂')
plt.plot(elements, union[1], 'g--', label='Union (A₂ ∪ B₂)')
plt.plot(elements, intersection[1], 'm--', label='Intersection (A₂ ∩ B₂)')
plt.plot(elements, algebraic_sum[1], 'y--', label='Algebraic Sum')
plt.plot(elements, algebraic_product[1], 'k--', label='Algebraic Product')
plt.plot(elements, bounded_sum[1], 'b:', label='Bounded Sum')
plt.plot(elements, bounded_difference[1], 'r:', label='Bounded Difference')
plt.title("Fuzzy Set Operations Visualization (Set 2)", fontsize=13)
plt.xlabel("Elements")
plt.ylabel("Membership Value")
plt.ylim(0, 1.1)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()