import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


df=pd.read_csv("C:/Users/admin/downloads/Admission_Predict.csv")
df.head()


df=df.select_dtypes(include=['int64','float64'])
X = df.drop("CGPA", axis=1)
y = df["CGPA"]


plt.figure(figsize=(8,6))
sns.scatterplot(
    data=df,
    x="GRE Score",
    y="TOEFL Score",
    hue="CGPA"
)
plt.title("Before PCA (Using First Two Features)")
plt.grid(True)
plt.show()


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=2)
pca_data = pca.fit_transform(X_scaled)
df_pca = pd.DataFrame(pca_data, columns=['PC1', 'PC2'])
df_pca["CGPA"] = y

print("Explained Variance Ratio:", pca.explained_variance_ratio_)


plt.figure(figsize=(8,6))
sns.scatterplot(
    data=df_pca,
    x="PC1",
    y="PC2",
    hue="CGPA"
)
plt.title("After PCA (2 Principal Components)")
plt.grid(True)
plt.show()