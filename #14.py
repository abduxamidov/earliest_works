# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
f_yosh = int(input("Yoshingiz nechada? >>> "))
if f_yosh<=4 or f_yosh>=60:
    print("Sizga kirish bepul!")
elif f_yosh<18:
    print("Sizga kirish 10.000 so'm! ")
elif f_yosh>=18:
    print("Sizga kirish 20.000 so'm! ")



















