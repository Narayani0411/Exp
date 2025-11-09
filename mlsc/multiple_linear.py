import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score


df=pd.read_csv("C:/Users/admin/downloads/Admission_Predict.csv")
df.head()

df.isna().sum()
df['CGPA']=df['CGPA'].fillna(df['CGPA'].mean())


X=df[["GRE Score","CGPA"]]
y=df["TOEFL Score"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)
y_pred


line_points = np.linspace(y_test.min(), y_test.max(), 100)
plt.plot(line_points, line_points, color='red', linewidth=2, label='Perfect Prediction Line')
plt.scatter(y_test, y_pred, color='blue')
plt.xlabel("Actual Math Scores")
plt.ylabel("Predicted Math Scores")
plt.title("Actual vs Predicted (Linear Regression)")
plt.show()


print(f"Model Score: {model.score(X_test,y_test)*100}")


print("Model Evolution")
print(f"mean squared error:{mean_squared_error(y_test,y_pred)}")
print(f"R2 score:{r2_score(y_test,y_pred)}")
print(f"Coefficient: {model.coef_}")
print(f"Intercept:{model.intercept_}")
print(f"Y={model.coef_}*X+{model.intercept_}")



y_pred=model.predict([[8,4]])
y_pred