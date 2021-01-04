# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
#for ism in ismlar:
 #   print(f"Salom, {ism} yaxshimisan? Nima gaplar?")

# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
#print("Kod", len(ismlar),"marta takrorlandi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
#royxat = list(range(11,101,2))
#kub_royxat = []
#for n in royxat:
#    kub_royxat.append(n**3)
#print(royxat)
#print(kub_royxat)

#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
#kinolar = []
#print("5ta eng sevimli kinolaringizni kiriting")
#for n in range(0,5):
#    kinolar.append(input(f"{n+1}-kinongizni kiriting "))
#print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
odam = []
l = len(odam)
l = int(input("Bugun necha kishi bilan suhbat qurdingiz?>>> ")) 
for n in range(l):
    odam.append(input(f"{n+1}-odamingizni kiriting "))
print(odam)


















