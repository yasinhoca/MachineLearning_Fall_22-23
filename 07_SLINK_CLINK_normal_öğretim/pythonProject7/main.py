# csv dosyalarını okumak için
import pandas as pd

# 2 boyutlu grafik oluşturmak için
import matplotlib.pyplot as plt

# csv dosyamızı okuduk.
data = pd.read_csv('Iris.csv')

# Veriler
v = data.iloc[:,1:-1].values

# AgglomerativeClustering sınıfını import ettik
from sklearn.cluster import AgglomerativeClustering

# AgglomerativeClustering sınıfından bir nesne ürettik
# n_clusters = Ayıracağımız küme sayısı
# linkage ve affinity = mesafe ölçüm yöntemleri
# linkage ve affinity parametrelerinin değiştirilmesi başarı oranını etkiler.
ac = AgglomerativeClustering(n_clusters=3, affinity='euclidean',linkage='ward')

# Kümeleme ve tahmin işlemi yap
predict = ac.fit_predict(v)

# Dendogram grafiği gösterimi
import scipy.cluster.hierarchy as sch

# v = verilerimiz
# method = AgglomerativeClustering'in linkage parametresi ile aynı parametreyi veriyoruz. ( 'ward' )
dendrogram = sch.dendrogram(sch.linkage(v,method='ward'))
plt.show()

# Grafik şeklinde ekrana basmak için
plt.scatter(v[predict==0,0],v[predict==0,1],s=50,color='red')
plt.scatter(v[predict==1,0],v[predict==1,1],s=50,color='blue')
plt.scatter(v[predict==2,0],v[predict==2,1],s=50,color='green')
plt.title('Hierarchical Clustering Iris Dataset')
plt.show()