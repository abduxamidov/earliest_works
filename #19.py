# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

b_son=int(input("Istalgan butun sonni kiriting: "))
a_son=list(range(2, 11))
for k in a_son:
    if b_son%k==0:
        print(f"{b_son} soni {k}ga qoldiqsiz bo'linadi!")














