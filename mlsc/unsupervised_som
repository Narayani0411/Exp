
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from minisom import MiniSom

# Load data
iris = load_iris()
X = iris.data
y = iris.target

# Scale data
X_scaled = MinMaxScaler().fit_transform(X)

# Create SOM (Unsupervised)
som = MiniSom(x=7, y=7, input_len=X.shape[1], sigma=1.0, learning_rate=0.5)
som.random_weights_init(X_scaled)

print("Training Unsupervised SOM...")
som.train_random(X_scaled, 1000)
print("Training completed.")

# Plot U-Matrix
plt.figure(figsize=(8, 8))
plt.pcolor(som.distance_map().T, cmap='bone_r')
plt.colorbar()

# Plot labels on neuron winners
for i, x in enumerate(X_scaled):
    w = som.winner(x)
    plt.text(w[0] + 0.5, w[1] + 0.5,
             str(y[i]),
             color=plt.cm.rainbow(y[i] / y.max()),
             fontsize=12)

plt.title("Unsupervised SOM (U-Matrix + Labels)")
plt.show()