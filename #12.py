# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
#    if car=="gm":
#        print(car.upper())
 #   else:
 #       print(car.title())
        
# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']   
#for car in cars:
   # if car!="gm":        
  #      print(car.title())  
  #  else:
  #      print(car.upper())

# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, 
# Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. 
# Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.        
#login=input("loginni kiriting>>>")
#if login=="admin".lower():
#    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
#else:
#    print(f"Xush kelibsiz,{login}!")  
    
# Foydalanuvchidan 2 ta son kiritishni so'rang.
#  Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.    
#print("Ikkita son kiriting!\n")    
#a= []
#b=[]
#for son in range(1):
  #  print(a.append(int(input("1-sonni kiriting\n>>>"))))
 #   print(b.append(int(input("2-sonni kiriting\n>>>"))))
 #   if a == b:
  #      print("Sonlar bir-biriga teng ekan!")
  #  else:
  #      print("Turli xil sonlar!")
        
# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.         
#son = int(input("Istalgan sonni kiriting\n>>>"))
# if son<0:
#    print("Son manfiy!")
#else:
#   print("Son musbat!")
 
# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
n = int(input("Son kiriting\n>>> "))
if n>0:
     print("Siz kiritgan sonning ildizi ",n**1//2," ga teng")
else:
    print("Iltimos faqat musbat son kiriting!")

























