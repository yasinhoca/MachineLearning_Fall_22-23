# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-xK0og65hkmP6nZU4L6CK_7Wjtq_90Os

Destek Vektör Makinası uygulamasına örnek olarak, çokça duyulan ve kullanılan Iris Veri Seti üzerinden basit bir örnek ile çözümlemelerde bulunalım.

Iris Veri Seti 3 Iris bitki türüne (Iris Setosa, Iris Virginica ve Iris Versicolor) ait, her bir türden 50 örnek olmak üzere toplam 150 örnek sayısına sahip bir veri setidir.

Iris Veri Seti içerisinde;

Sınıflar (Türler);
Iris Setosa,
Iris Versicolor,
Iris Virginica.

Veri Özellikleri (Ortak Özellikler);
Sepal Uzunluk (cm),
Sepal Genişlik (cm),
Petal Genişliği (cm)
Petal Uzunluk (cm).
özellik ve değerleri bulunmaktadır.

Dilerseniz hızlıca analizimizi gerçekleştirmek için adımlarımızı uygulamaya başlayalım.
"""

#1-Gerçekleştireceğimiz analizler için kullanacağımız kütüphaneleri sırası ile projemize dahil edelim;
from sklearn import datasets    
from sklearn import svm       
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

#2-Modeli oluşturmak için üzerinde çalışacağımız Iris Veri Seti’ni proje içerisine aktaralım;
iris = datasets.load_iris()

#3-Sepal Uzunluk ve Sepal Genişlik üzerinden türler arasındaki korelasyonları gözlemlemek için keşif verisi adımlarımızı sırası ile gerçekleştirelim;
def visualize_sepal_data():
  iris = datasets.load_iris()
  X = iris.data[:, :2]
  y = iris.target
  plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm)
  plt.xlabel('Sepal length')
  plt.ylabel('Sepal width')
  plt.title('Sepal Width & Length')
  plt.show()
visualize_sepal_data()

#keşif verilerini işleyerek grafik üzerinde görselleştirelim;

#4-Sepal Uzunluk ve Sepal Genişlik üzerinde gerçekleştirdiğimiz türler arasındaki korelasyonları gözlemlemek için keşif verisi adımlarını şimdi Petal Uzunluk ve Petal Genişlik için gerçekleştirelim;
def visualize_petal_data():
  iris = datasets.load_iris()
  X = iris.data[:, 2:]
  y = iris.target
  plt.scatter(X[:, 0], X[:, 1], c=y)
  plt.xlabel('Petal length')
  plt.ylabel('Petal width')
  plt.title('Petal Width & Length')
  plt.show()
visualize_petal_data()

#keşif verilerini işleyerek grafik üzerinde görselleştirelim;

#5-Çiçeğin ait olduğu sınıfın türünü tahmin etmek için ilk iki özelliği (Sepal Uzunluk/Genişlik) kullanarak bir DVM / SVM modeli oluşturalım.
X = iris.data[:, :2]
y = iris.target

#ALTERNATIF KULLANIM.
# X = iris.data[:, 2:]
# y = iris.target

#6-Çeşitli çekirdekler kullanarak DVM / SVM karar sınırlarını çizmek için bir model ağacı oluşturalım;
def plotSVM(title):

       x_min, x_max = X[:, 0].min() -1, X[:, 0].max() + 1
       y_min, y_max = X[:, 1].min() -1, X[:, 1].max() + 1
       h = (x_max / x_min)/100
       xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
       np.arange(y_min, y_max, h))
       plt.subplot(1, 1, 1)
       Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
       Z = Z.reshape(xx.shape)
       plt.contour(xx, yy, Z,alpha=0.8)
       plt.scatter(X[:, 0], X[:, 1], c=y)
       plt.xlabel("Sepal length")
       plt.ylabel("Sepal width")
       plt.xlim(xx.min(), xx.max())
       plt.title(title)
       plt.show()

#7-Oluşturduğumuz yapımız için Lineer ve Lineer Olmayan (Polinomal ve Gauss) modellemeler üzerinden çekirdek işlemleri gerçekleştirelim;
kernels = ["linear", "rbf", "poly"]
for kernel in kernels:
       svc = svm.SVC(kernel=kernel).fit(X, y)
       plotSVM("kernel=" + str(kernel))

#çekirdek işleme işlemlerimizi gerçekleştirdikten sonra sınıflandırma modelimizi görselleştirirsek;

"""çıktılarına ulaşırız."""

#8-Farklı Gama (Gamma : γ) değerleri (0.1, 1, 10, 100) üzerinden çeşitli çekirdekleri gözlemleyerek hiperparametre ayarı oluşturalım;
gammas = [0.1, 1, 10, 100]
for gamma in gammas:
       svc = svm.SVC(kernel='rbf', gamma=gamma).fit(X, y)
       plotSVM('gamma=' + str(gamma))

"""Genel olarak gama değeri arttıkça model uyumunda artış gözlemlenmektedir."""

#9- C* (Hata Değeri / Ceza Değeri) parametresi üzerinde belirli değerler (0.1, 1, 10, 100, 1000) belirleyerek gözlemde bulunalım.

#C*=Sorunsuz bir karar sınırı ile eğitim noktalarının doğru şekilde sınıflandırılması arasındaki dengeyi kontrol eder.
cs = [0.1, 1, 10, 100, 1000]
for c in cs:
       svc = svm.SVC(kernel='rbf', C=c).fit(X, y)
       plotSVM('C=' + str(c))

"""Küçük veri kümelerinde C* (Hata Değeri / Ceza Değeri) parametresi  göz ardı edilebilir.
Fakat yüksek ölçekteki veri kümelerinde bu büyük hatalara neden olabilir. 
"""

#10-Son olarak ise uyguladığımız modelin doğruluğunu çekirdek modelinde lineer yapıyı (Doğruluk Yüzdesi) baz alarak hesaplayalım;
lin_svc = svm.SVC(kernel='linear').fit(X,y)
predictions = lin_svc.predict(iris.data[:, :2])
accuracy_score(predictions, iris.target)

"""Oluşturduğumuz DVM / SVM modelimiz bize %82 oranında doğruluk değeri sağlamaktadır.

Burada daha hassas Gama ve C değerleri saptanarak doğruluk değeri optimuma yükseltilebilir.
Böylelikle oluşturacağımız sınıflandırma işlemi için daha net/doğru sonuçlar elde edebiliriz.

İlgili verilerin işlenmesinin yanı sıra görselleştirilmesi de analiz işlemleri adına önem arz etmektedir.
"""