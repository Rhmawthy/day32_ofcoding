#program mencari bilangan terbesar dan terkecil
bil1 = int(input("masukkan nilai:"))
bil2 = int(input("masukkan nilai:"))
bil3 = int(input("masukkan nilai:"))

#nilai terbesar
if bil1 > bil2 and bil1 > bil3:
    print ("nilai terbesar",bil1)
elif bil2 > bil1 and bil2 > bil3:
    print ("nilai terbesar",bil2)
else:
    print ("nilai terbesar",bil3)
    
#nilai terkecil
if bil1 < bil2 and bil1 < bil3:
    print ("nilai terkecil",bil1)
elif bil2 < bil1 and bil2 < bil3:
    print ("nilai terkecil",bil2)
else:
    print ("nilai terkecil",bil3)
    
