fruitsTuple = ("apple","banana","cherry","kiwi")
fruitsList  = ["apple","banana","cherry","kiwi"]
print(fruitsTuple[0:3])
print(fruitsList[0])
#เปลี่ยนค่าในtuple
fruitsList[1]="mango"  #เปลี่ยนในlist
print(fruitsList) 
#ในTupleไม่สามารถเปลี่ยนค่าโดยตรงได้ 
x = list(fruitsTuple)
x[1]="mango"
fruitsTuple = tuple(x)
print(fruitsTuple)
#เพิ่มค่าในTuple
x = list(fruitsTuple)
x[1]="orange"
fruitsTuple = tuple(x)
print(fruitsTuple)
#ลดค่าในTuple
x = list(fruitsTuple)
x.remove("kiwi")
fruitsTuple = tuple(x)
print(fruitsTuple)
x = range(3, 20)
for n in x:
    print(n)
x = range(3, 20, 2)
for n in x:
    print("step3:",n)
#นายกิตติ มไนนิล 21 6/9