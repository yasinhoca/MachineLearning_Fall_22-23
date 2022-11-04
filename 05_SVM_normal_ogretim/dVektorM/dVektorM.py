#Formul = (W,Xi)+@0(teta)>=+1 ise sınıf = +1,(W,Xi)+@0(teta)<=-1 ise sınıf = -1
KoordinatX=int(input("Sınıflandırmak istediğiniz objenin X koordinatını giriniz= "))
KoordinatY=int(input("Sınıflandırmak istediğiniz objenin Y koordinatını giriniz= "))
teta=int(input("Teta değerini giriniz= "))
w=int(input("W değerini giriniz= "))
Xi=int(input("Xi değerini giriniz= "))
Formul=(w*KoordinatX)+(Xi*KoordinatY)-teta
print("Sınıflandırdığımız Objenin konumu= ",Formul)
if Formul >=1:
    print("Obje Pozitif Sınıftadır")
elif Formul <=-1:
    print("Obje Negatif Sınıftadır")
elif Formul == 0:
    print("Obje Hiper düzlemin üstündedir")