fruits = ["apple" , "banana" , "cherry" , "orange"]
#เปลี่ยนค่าในlist
fruits[1] = "blackcurrant"
print(fruits)
fruits[1:3] = ["kiwi", "watermelon", "melon"]
print(fruits)
#เพิ่มค่าในlist
fruits .append("mango")
print(fruits)
fruits.insert(2,"durian")
print(fruits)
tropical=['papaya', 'pineapple']
fruits.extend(tropical)
print(fruits)
#ลบค่าในlist
fruits.remove("durian")
print(fruits)
fruits.pop(3)
print(fruits)
#del fruits ลบทุกอย่างในlist
#เรียงค่าในlist
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
#กิตติ มไนนิล 6/9 21