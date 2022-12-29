#Random Forest Regresyon

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#2.veri yukleme
veriler = pd.read_csv('maaslar.csv')
x = veriler.iloc[:,1:2]
y = veriler.iloc[:,2:]
X = x.values
Y = y.values
#3.verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler
sc1=StandardScaler()
x_olcekli = sc1.fit_transform(X)
sc2=StandardScaler()
y_olcekli = np.ravel(sc2.fit_transform(Y.reshape(-1,1)))
#4.Karar ağacı
from sklearn.tree import DecisionTreeRegressor
r_dt = DecisionTreeRegressor(random_state=0)
r_dt.fit(X,Y)
Z = X + 0.5
K = X - 0.4
plt.scatter(X,Y, color='red')
plt.plot(x,r_dt.predict(X), color='blue')
plt.plot(x,r_dt.predict(Z),color='green')
plt.plot(x,r_dt.predict(K),color='yellow')
#5.Random forest regresyon
from sklearn.ensemble import RandomForestRegressor
rf_reg=RandomForestRegressor(n_estimators = 10,random_state=0)
rf_reg.fit(X,Y.ravel())
#6.Verilerini görselleştirmek için bu kısmı yazın
plt.scatter(X,Y,color='red')
plt.plot(X,rf_reg.predict(X),color='blue')
plt.plot(X,rf_reg.predict(Z),color='green')
plt.plot(x,r_dt.predict(K),color='yellow')
plt.show()