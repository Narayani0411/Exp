
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from minisom import MiniSom

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Scale data between 0 and 1
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Create SOM grid (7x7)
som = MiniSom(
    x=7, 
    y=7, 
    input_len=X_scaled.shape[1], 
    sigma=1.0,
    learning_rate=0.5
)

# Initialize random weights
som.random_weights_init(X_scaled)

print("Training SOM...")
som.train_random(X_scaled, num_iteration=1000)
print("Training completed.")

# Plot SOM
plt.figure(figsize=(8, 8))

# U-Matrix (shows distances between neurons)
plt.pcolor(som.distance_map().T, cmap='bone_r')
plt.colorbar()

# Plot data labels on SOM
for i, x in enumerate(X_scaled):
    w = som.winner(x)  # winning neuron
    plt.text(
        w[0] + 0.5,
        w[1] + 0.5,
        str(y[i]),
        color=plt.cm.rainbow(y[i] / y.max()),
        fontsize=12,
        fontweight='bold'
    )

plt.title("Self-Organizing Map (SOM) on Iris Dataset")
plt.xlim([0, 7])
plt.ylim([0, 7])
plt.show()