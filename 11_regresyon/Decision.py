#Decision regresyon

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#2.Veri yukleme
veriler = pd.read_csv('maaslar.csv')
x = veriler.iloc[:,1:2]
y = veriler.iloc[:,2:]
X = x.values
Y = y.values
#3.Desicion Tree Regresyonu
from sklearn.tree import DecisionTreeRegressor
r_dt = DecisionTreeRegressor(random_state=0)
r_dt.fit(X,Y)
Z = X + 0.5
K = X - 0.4
#4.Buradayı yazarak verilerinizi görebilirsiniz.
plt.scatter(X,Y, color='red')
plt.plot(x,r_dt.predict(X), color='blue')
plt.plot(x,r_dt.predict(Z),color='green')
plt.plot(x,r_dt.predict(K),color='yellow')
plt.show()