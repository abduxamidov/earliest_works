# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

mahsulot =["guruch", "shakar", "piyoz", "go'sht", "yog'", "kortoshka", "non", "tuz", "sovun", "gugurt"]
savat = []
bor_mahsulot =[]
yoq_mahsulot =[]
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni kiriting! >>> "))
for buyurtma in savat:
        if buyurtma in mahsulot:
            bor_mahsulot.append(buyurtma)
            
        elif buyurtma not in mahsulot:
            yoq_mahsulot.append(buyurtma) 
if len(yoq_mahsulot)==0:
   print("Siz so'ragan barcha mahsulotlar do'konimizda bor!")
elif len(bor_mahsulot)==0:
   print("Siz so'ragan mahsulotlar do'konimizda yo'q!")                 
elif len(yoq_mahsulot)!=0 or len(bor_mahsulot)!=0:
    print("Do'konimizda quyidagi mahsulotlar yo'q!")
    for yoqlar in yoq_mahsulot:
        print(f"{yoqlar}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    