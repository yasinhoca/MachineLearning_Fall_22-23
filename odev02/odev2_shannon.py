import math
s = input("Ad Soyad giriniz:")

s = s.replace(" ","")

liste = []

for i in s:
    liste.append(i)

print(liste)
k = set(liste)
print(k)

d = {}

for i in k:
    adet = liste.count(i)
    oran = adet/len(liste)
    d.update({i:oran})

print(d)

shannon = 0

for i in d:
    v = d[i]
    shannon += v*math.log(v,2)

shannon *=-1;

print(shannon)

bs = math.ceil(shannon)
print("Bit sayısı = ", bs)

dk = list(k)

b = []
for i in range(int(math.pow(2,bs))):
    a = bin(i)[2:]
    b.append(a)

dk.sort()
print(dk)
print(b)

for i in range(len(b)):
    for j in range(bs-len(b[i])):
        b[i] = "0"+b[i]

print(b)

coded = ""
for i in liste:
    coded += b[dk.index(i)]

print(coded)