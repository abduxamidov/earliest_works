# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ["manti", "norin", "somsa", "osh", "lagmon"]

# nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]
print(nonushta)
# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove("norin")
nonushta.remove("osh")
nonushta.append("tuxum")
nonushta.append("kolbasa")
 
# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar)
print(nonushta)

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
nonushta[0]= "qaymoq va non"
print(nonushta)













