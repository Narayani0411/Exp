import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler

df=pd.read_csv("C:/Users/admin/downloads/Admission_Predict.csv")
df.head()

X=df[["CGPA","TOEFL Score"]]
y=df["GRE Score"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

model=LogisticRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

y_pred

print(f"Model Accuracy:{accuracy_score(y_test,y_pred)}")
print(f"Confusion matrix:{confusion_matrix(y_test,y_pred)}")
print(f"Classification report:\n{classification_report(y_test,y_pred)}")

plt.figure(figsize=(8,6))
plt.scatter(X_test[:,0],X_test[:,1],c=y_pred,cmap="bwr")
plt.title("Logistic Regression")
plt.xlabel("CGPA")
plt.ylabel("GRE Score")
plt.show()