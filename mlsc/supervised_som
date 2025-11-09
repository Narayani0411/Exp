
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from minisom import MiniSom

# Load data
iris = load_iris()
X = iris.data
y = iris.target

# Scale
X_scaled = MinMaxScaler().fit_transform(X)

# Train SOM
som = MiniSom(x=7, y=7, input_len=X.shape[1], sigma=1.0, learning_rate=0.5)
som.random_weights_init(X_scaled)
som.train_random(X_scaled, 1000)

# Convert samples to neuron positions (Supervised encoding)
mapped = np.array([som.winner(x) for x in X_scaled])
mapped = mapped.reshape(len(X), 2)  # (winner_x, winner_y)

# Train-Test split
X_train, X_test, y_train, y_test = train_test_split(mapped, y, test_size=0.2, random_state=42)

# Train classifier (KNN)
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)

# Predict
y_pred = clf.predict(X_test)

print("Supervised SOM Accuracy:", accuracy_score(y_test, y_pred))

# Plot SOM + labels
plt.figure(figsize=(8, 8))
plt.pcolor(som.distance_map().T, cmap='bone_r')
plt.colorbar()

for i, m in enumerate(mapped):
    plt.text(m[0] + 0.5, m[1] + 0.5, str(y[i]),
             color=plt.cm.rainbow(y[i]/y.max()),
             fontsize=12)

plt.title("Supervised SOM (SOM + KNN Classifier)")
plt.show()