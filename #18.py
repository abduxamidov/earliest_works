# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
login=["olim", "anvar", "doston", "umar", "lola"]
y_login=[]
y_login=input("Yangi login kiriting >>> ")
if y_login.lower() in login:
    print("Buday login band! Iltimos boshqa login kiriting!")
else:
    print("Xush kelibsiz!")