import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# ---------- Input Data (3×3 Matrix) ----------
# Example 3×3 matrix
data = np.array([
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
])

print("Original Data:\n", data)

# ---------- Sub-Q1: Preprocessing ----------
scaler = StandardScaler()
data_std = scaler.fit_transform(data)
print("\nStandardized Data:\n", data_std)

# ---------- Sub-Q2: PCA Reduction ----------
# Reduce 3D → 2 components
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_std)

print("\nPCA Reduced Data (2D):\n", data_pca)
print("Explained Variance Ratio:", pca.explained_variance_ratio_)

# ---------- Sub-Q3: Plot ----------
plt.figure(figsize=(10,5))

# Plot original standardized 3D data (project first 2 features)
plt.subplot(1,2,1)
plt.scatter(data_std[:,0], data_std[:,1], s=120, color='blue')
plt.title("Original Data (Standardized)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)

# Plot PCA output (2D)
plt.subplot(1,2,2)
plt.scatter(data_pca[:,0], data_pca[:,1], s=120, color='red')
plt.title("PCA Reduced Data (2D)")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.grid(True)

plt.tight_layout()
plt.show()