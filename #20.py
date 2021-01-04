# # otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :
# otam ={"ism":"Jamshid", "t_yil":1977, "t_joy":"Buxoro"}
# print(f"Otamning ismi {otam['ism'].title()},{otam['t_yil']}-yilda {otam['t_joy']}da tug'ilgan")

# # Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: 
# s_taomlar={
#     'otam':'osh',
#     'onam':'norin',
#     'ukam':'lagmon',
#     'singlim':'somsa'
#     }
# print(f"Otamning sevimli taomi {s_taomlar['otam']}")
# print(f"Onamning sevimli taomi {s_taomlar['onam']}")
# print(f"Ukamning sevimli taomi {s_taomlar['ukam']}")     

# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
atama = {
    'integer':'butun son',
    'float':'onli kasr',
    'string':'matn',
    'dictionary':'lugat',
    'input':'qoymoq',
    'print':'nashr qilmoq',
    'list':'royxat',
    'error':'xatolik',
    'if':'agar',
    'else':'modomiki'
    }

# # Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

# print("Biror so'zni kiriting!")
# nom = input(">>>> ")
# nom = atama.get('lol', 'bunday nom mavjud emas')
# print(f"{nom} so'zining tarjimasi - {atama[nom]}")

# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
nom = input("Biror so'zni kiriting: ")
if nom in atama:
    print(f"Siz so'ragan so'zning tarjimasi -{atama[nom]}")
else:
    print("Siz so'ragan so'z mavjud emas!")




























