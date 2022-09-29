str1 = open('m1.txt', 'r').read()
str2 = open('m2.txt', 'r').read()

str1 = str1.replace(".","")
str1 = str1.replace(",","")
str1 = str1.replace("'","")
l1 = list(str1.split(" "))
print(l1)
print(len(l1))

str2 = str2.replace(".","")
str2 = str2.replace(",","")
str2 = str2.replace("'","")
l2 = list(str2.split(" "))
print(l2)
print(len(l2))

s1 = set(l1)
print(s1)
print(len(s1))
s2 = set(l2)
print(s2)
print(len(s2))

st = set.union(s1,s2)
print(st)
print(len(st))

ts = len(s1)+len(s2)
print("İki metin için tekil sözcük sayısı = ", ts)
tss = len(st)
print("Birleşim sonrası tekil sözcük sayısı = ",tss)
fark = ts - tss
print("Fark = ", fark)
benzeme = (fark*100)/tss
print("Benzeme oranı = %",benzeme)

