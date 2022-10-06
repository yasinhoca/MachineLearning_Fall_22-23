import re
listeNormal = ("sevgili","sevgili","sevgili","sevgili","sevgili","sevgili","sevgili","sevgili","arkadaş","arkadaş","arkadaş","arkadaş","arkadaş","yemek","yemek","yemek","para")
listeSpam = ("sevgili","sevgili","arkadaş","yemek","para","para","para","para")


spamMesajSayısı = int(input("Normal Mesaj Sayısı: "))
normalMesajSayısı = int(input("Spam Mesaj Sayısı: "))
toplamMesajSayısı = spamMesajSayısı+normalMesajSayısı

normalMesajOranı = normalMesajSayısı/toplamMesajSayısı
#print(normalMesajOranı)

spamMesajOranı = spamMesajSayısı/toplamMesajSayısı
#print(spamMesajOranı)

ls = set(listeNormal)
ls2 = set(listeNormal)

normalMesajKelimeSayısı = {}
spamMesajKelimeSayısı = {}
for x in ls:
    a = listeNormal.count(x)/len(listeNormal)
    normalMesajKelimeSayısı[x] = a
#print(normalMesajKelimeSayısı)
for x in ls2:
    a = listeSpam.count(x)/len(listeSpam)
    
    spamMesajKelimeSayısı[x] = a
#print(spamMesajKelimeSayısı)


mesaj = input("Gelen Mesajı Giriniz: ")
mesajKelimeleri = re.split("\s",mesaj)
oran1=0.6666666666666666
for i in mesajKelimeleri:
    oran1 *= normalMesajKelimeSayısı[i]
oran2=0.3333333333333333
for i in mesajKelimeleri:
    oran2 *= spamMesajKelimeSayısı[i]

print("\n","*"*20)
print("Gelen Mesajınızın Normal İleti Olma Olasılığı: ",oran1)
print("Gelen Mesajınızın Spam Olma Olasılığı: ",oran2)
print("\n","*"*20)