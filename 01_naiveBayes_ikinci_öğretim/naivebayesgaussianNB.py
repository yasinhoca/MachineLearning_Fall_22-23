#Veri setini yüklemek için kullanacağımız kısım   
#sklearn ismindeki kütüphaneden Iris veri setini çeke bilmek için oluşturuldu
from sklearn import datasets
#Sınıflandırma ve karşılıklı matris içinkullanıcağımız yer 
from sklearn import metrics 
#Gaussian naive bayes eklentisi 
from sklearn.naive_bayes import GaussianNB
#Çiçek türlerinden oluşan Irsi veri seti yüklendi 
veri_seti= datasets.load_iris()
#Gaussian NB sayesinde veri ve hedef özellik  belirtilerek model eğitildi 
egitim_modeli= GaussianNB()
#Target (Hedef özellikler) ile bizim var olan kullanıcağımız verileri.
# Normalizasyon yapmamız gerekiyor ki hedef olan kısımları doğru tahmin edebilelim. 
egitim_modeli.fit(veri_seti.data, veri_seti.target)
#Beklenen (Target) ve tahmin edilen sonuçlar hesaplandı(veri_seti.data) 
beklenen=veri_seti.target
hesaplanan=egitim_modeli.predict(veri_seti.data)
#Sınıflandırma sonuçları ile karşılıklı matris hesaplandı 
siniflandirma_matrisi= metrics.classification_report(beklenen, hesaplanan)
karisiklik_matrisi=metrics.confusion_matrix(beklenen, hesaplanan)
#Sınıflandırma sonuçları ile karşılıklı matris ekrana yazıldı 
print('\nSınıflandırma Matrisi\n')
print(siniflandirma_matrisi)
print('\nKarşılık Matrisi\n')
print(karisiklik_matrisi)


