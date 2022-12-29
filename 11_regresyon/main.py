#Basit Doğrusal Regresyon
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
veriler = pd.read_csv('maaslar.csv')
x = veriler.iloc[:,1:2]
y = veriler.iloc[:,2:]
X = x.values
Y = y.values


from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,Y)

plt.scatter(X,Y,color='red')
plt.plot(x,lin_reg.predict(X), color = 'blue')
plt.show()