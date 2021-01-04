dict_2 = {"o'zbekiston":"toshkent",
          "rossiya":"moskva",
          "aqsh":"vashington",
          "xitoy":"pekin",
          "kanada":"ottava",
          "tojikiston":"dushanbe",
          "italya":"rim"
          }
davlat = input("Qaysi davlatni poytaxtini bilishni xoxlaysiz?: ")
if davlat.lower() in dict_2:
    print(f"{davlat.title()}ning poytaxti {dict_2[davlat].title()}!")
else:
    print("Bizda bunday davlatning ma'lumoti yo'q!")
    

    