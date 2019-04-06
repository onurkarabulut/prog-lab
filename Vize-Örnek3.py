#verilen kelime tersten okunuşu ile aynı ise True farklı ise False döndüren fonksiyon
def testet(kelime):
    k=[]
    k=list(kelime)
    kt=[]
    for i in range(len(kelime)-1,-1,-1):
        kt.append(kelime[i])       
    if(k==kt):
        Durum=True
        return Durum
    else:
        Durum=False
        return Durum
klm="ses"
a=testet(klm)
print(a)
klm2="onur"
b=testet(klm2)
print(b)



