import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#2.Veri yukleme
veriler = pd.read_csv('maaslar.csv')
x = veriler.iloc[:,1:2]
y = veriler.iloc[:,2:]
X = x.values
Y = y.values
#3.Verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler
sc1=StandardScaler()
x_olcekli = sc1.fit_transform(X)
sc2=StandardScaler()
y_olcekli = np.ravel(sc2.fit_transform(Y.reshape(-1,1)))
#4.SV Regresyon
from sklearn.svm import SVR
svr_reg = SVR(kernel='rbf')
svr_reg.fit(x_olcekli,y_olcekli)
#5.Burayı yazarak verilerinizin çıktısını görebilirsiniz.
plt.scatter(x_olcekli,y_olcekli,color='red')
plt.plot(x_olcekli,svr_reg.predict(x_olcekli),color='blue')
plt.show()