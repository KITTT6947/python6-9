for index in range(1,11,1):
    print(index)
    
#loop กับ list 
List1 = ['Kitti', 'Jojo','kuku']
for element in List1:
    print(element)
    
#loop กับ dic
Dic = {'name':'joshep','age':50,'job':'mnage'}
for key,value in Dic.items():
    print(key,':',value)
List2=[{'name':'joshep','age':50,'job':'mnage'},
       {'name':'kiti','age':18,'job':'popstar'},
       {'name':'mark','age':25,'job':'teacher'},
       {'name':'Tuu','age':66,'job':'soldier',}]
for element in List2:
    for key, value in element.items():
        print(key,value)
i = 1
while i<2:
    print(i)
    i+=1
name =input("ชื่อ:")
print(name)