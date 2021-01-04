## ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar = ['otabek', 'davron', 'oybek']

## Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
print('Salom '+ ismlar[0].title() + ' qalaysan, nimalar qilyapsan?')
print('salom '+ ismlar[1].title()+' bugun choyxona bormi?')
print('Yaxshimisan '+ismlar[2].title()+' nimalar qilyapsan?')

## sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
sonlar = [3, -4, 6, 2.3]

## Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
print(sonlar[0] + sonlar[-1])
print(sonlar[1]- sonlar[2])
print(sonlar[2]*sonlar[1])
print(sonlar[-2]/ sonlar[0])

sonlar[0] = 5
sonlar[-1] = 5.6
print(sonlar)
sonlar[0] = sonlar[3]
sonlar[1]=sonlar[2]
print(sonlar)

## t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan 
#tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 
t_shaxslar = ['temur', 'alisher', "ulug'bek"]
z_shaxslar = ["shavkat", "xushnudbek", "putin"]

## Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib
# (.pop()), quyidagi ko'rinishda chiqaring:

print("men tarixiy shaxslardan ".capitalize()+t_shaxslar[0].title()+", zamonaviy shaxlardan esa "+z_shaxslar[0].title()+", bilan suhbat qurishni hohlar edim!")

## friendsnomli bo'sh ro'yxat tuzing va
# unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 
friends =[]
friends.append(ismlar)
friends.append("Islom")
friends.append("Hamdi")
friends.append("Abdulaziz")
friends.append("Ismoil")
print(friends)

## Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
friends.remove("Islom")
friends.remove("Ismoil")

print(friends)

## Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.insert(0, "Mahmud")
friends.insert(1, "Ahad")
friends.insert(-1, "Murod")
print(friends)

## Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari
# yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, 
#mehmonlar ro'yxatiga qo'shing.
mehmonlar = friends.pop(0)
mehmonlar = friends.pop(1)
mehmonlar = friends.pop(2)

















