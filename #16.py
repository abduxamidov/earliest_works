#  mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
#  Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni 
#  so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa
#  "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

mahsulot =["guruch", "shakar", "piyoz", "go'sht", "yog'", "kortoshka", "non", "tuz", "sovun", "gugurt"]
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni kiriting! >>> "))
for buyurtma in savat:
        if buyurtma in mahsulot:
            print(f"Do'konimizda {buyurtma} mahsuloti bor!")
        else:
            print(f"Do'konimizda {buyurtma} mahsuloti yo'q!")












