menu ={"osh":14000,
       "somsa":5000,
       "kabob":18000,
       "lavash":15000,
       "chuchvara":14000,
       "sho'rva":10000,
       "lag'mon":14000,
       "norin":15000,
       "hasib":14000,
       }
print("uchta taom buyurtma bering!!!".upper())  
buyurtma=[]
for n in range(3):
    taom=buyurtma.append(input(f"{n+1}-taomni kiriting!\n>>> "))
for taom in buyurtma:
    if taom in menu:
        print(f"{taom.title()}ning narxi {menu[taom]}")
    else:
        print(f"Kechirasiz, menyuda {taom} yo'q!")









































