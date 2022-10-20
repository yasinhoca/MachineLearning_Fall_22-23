a1 = [0,0,0,0,0,0,1,1,1,1]
a2 = [0,0,0,0,1,1,0,0,1,1]
a3 = [0,0,1,1,0,1,0,1,0,1]
a4 = [0,1,0,1,0,0,1,1,0,1]
cikti =  [0,1,1,0,1,0,0,1,0,0]
agirlik = [1.20,1.80,1.40,1.50]
fi = 0
lmbda = 0.3
NET = 0
output = 0

def net_hesapla(i):
    NET = a1[i]*agirlik[0]+a2[i]*agirlik[1]+a3[i]*agirlik[2]+a4[i]*agirlik[3];
    return NET

def perceptron_cikti(net):
    if net>fi:
       output=1
    else:
       output=0
    return output

def agirliklari_yeniden_hesapla(o,i):
    if o != cikti[i]:
        agirlik[0] = agirlik[0] - lmbda * a1[i]
        agirlik[1] = agirlik[1] - lmbda * a2[i]
        agirlik[2] = agirlik[2] - lmbda * a3[i]
        agirlik[3] = agirlik[3] - lmbda * a4[i]

for i in range(1):
    for j in range(len(cikti)):
        net_hesapla(j);
        op = perceptron_cikti(j)
        agirliklari_yeniden_hesapla(op,j)

print("Eğitim tamamlandı!\nEğitim sonrası ağırlıklar:")
print(agirlik)

g1, g2, g3, g4 = input("Lütfen test değerlerini giriniz:").split()
a1[0]=int(g1) # girdileri ilk indislere yerleştiriyoruz
a2[0]=int(g2)
a3[0]=int(g3)
a4[0]=int(g4)
print(perceptron_cikti(net_hesapla(0))) # ilk indisten hesaplatıyoruz

