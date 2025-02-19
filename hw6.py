#Dudu KABAKÇI 


a = 256
b = 256
print(a is b)

#Pyhton'da -5 ile 256 arasındaki tamsayılar bellekte önbelleğe yani
#cache alınır.

#is operatörü iki değişkenin aynı bellek adresine sahip olup
#olmadığını kontrol eder 

# a ve b aynı bellekteki 256'yı kullanır, bu yüzden ilk ifade True döner.

c = 257
d = 257
print(c is d)

#257 önbelleğe yani cache alınmadığı için ayrı bellek adreslerinde saklanır.
#Bu nedenle ikinci ifade False döner.
