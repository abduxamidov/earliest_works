dict_2 = {"o'zbekiston":"toshkent",
          "rossiya":"moskva",
          "AQSh":"vashington",
          "xitoy":"pekin",
          "kanada":"ottava",
          "tojikiston":"dushanbe",
          "italya":"rim"
          }
print("Dunyo davlatlari".upper())
for key in sorted(dict_2):   
        print(key.title())
        
print("\n")
print("davlatlar poytaxti".upper())
for value in sorted(dict_2.values()):    
        print(value.title())















