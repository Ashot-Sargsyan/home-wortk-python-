'''Python Set add() Method'''

'''1)Set add() Method'''
# set1={'hundai','toyota','subaru'}
# set1.add('honda')#Add Добавляет элемент в набор
# print(set1)


'''2)Python Set clear() Method'''
# set1={'Bmw','Nissan','Lada'}
# set1.clear()#Clear Удаляет все элементы из набора
# print(set1)


'''3)Python Set copy() Method'''
# set1={'Hummer','Lexus','Tesla','Audi'}
# set2=set1.copy()#Copy Возвращает копию набора
# print('','set1 :',set1,'\n','set2 :',set2)


# '''4)Python Set difference() Method'''
# set1={'hundai','toyota','subaru','Audi'}
# set2={'Hummer','Lexus','Tesla','Audi'}
# set3=set1.difference(set2)#difference Сравнивает два сета или несколько и удаляет то что есть и вдругих сета и выводит то что осталось в нашем случае audi удаляем
# print('','set1 :',set1,'\n','set2 :',set2,'\n',set3)


'''5)Python Set difference_update() Method'''
# set1={'Bmw','Nissan','Lada','Lexus'}
# set2={'Hummer','Lexus','Tesla','Audi'}
# set1.difference_update(set2)#difference_update() Сравнивает два сета или несколько и удаляет то что есть и вдругих сета и выводит то что осталось в нашем случае audi удаляем
# print(set1)


'''6)Python Set discard() Method'''
# set1={'hundai','toyota','subaru','Audi'}
# set1.discard('toyota')#discard() Удалить указанный элемент
# print(set1)


'''7)Python Set intersection() Method'''
# set1={'Bmw','Nissan','Lexus','Toyota'}
# set2={'Hummer','Lexus','Toyota','Audi'}
# set3=set1.intersection(set2)#intersection() Выводит то что совпадает в сетах
# print(set3)

'''8)Python Set intersection_update() Method'''
# set1={'Bmw','Nissan','Lexus','Toyota'}
# set2={'Hummer','Lexus','Toyota','Audi'}
# set1.intersection_update(set2)#intersection_update() Выводит то что совпадает в сетах
# print(set1)


'''9)Python Set isdisjoint() Method'''
# set1={'Bmw','Nissan','Lexus','Toyota'}
# set2={'Hummer','Lexus','Toyota','Audi'}
# set3=set1.isdisjoint(set2)#Если есть совпадение в нескольких сетах False выводит и наоборот True
# print(set3)


'''10)Python Set issubset() Method'''
# set1={'Bmw','Nissan','Lexus','Toyota'}
# set2={'Hummer','Lexus','Toyota','Audi',}
# set3=set1.issubset(set2)#Если во втором сете нету то что есть в первом сете выводит False выводит и наоборот True
# print(set3)


'''11)Python Set issuperset() Method'''
# set1={'Bmw','Nissan','Lexus','Toyota','Hummer','Lexus','Toyota','Audi'}
# set2={'Hummer','Lexus','Toyota','Audi'}
# set3=set1.issuperset(set2)#Если в первом сете есть то что есть и во втором сете выводит True  и наоборот если нету False
# print(set3)


'''12)Python Set pop() Method'''
# set1={'Hummer','Lexus','Toyota','Audi'}
# set1.pop()#Удаляет последний элемент из сета 
# print(set1)


'''13)Python Set remove() Method'''
# set1={'Hummer','Lexus','Toyota','Audi'}
# set1.remove('Hummer')#Удаляет Hummer элемент из сета 
# print(set1)


'''14)Python Set symmetric_difference() Method'''
# set1={'Bmw','Nissan','Lexus','Toyota'}
# set2={'Hummer','Lexus','Toyota','Audi',}
# set3=set1.symmetric_difference(set2)#Удаляет совпадающие елементы из сета 
# print(set3)


'''15)Python Set symmetric_difference_update() Method'''
# set1={'Bmw','Nissan','Lexus','Toyota'}
# set2={'Hummer','Lexus','Toyota','Audi',}
# set1.symmetric_difference_update(set2)#Удаляет совпадающие елементы из сета
# print(set1)


'''16)Python Set union() Method'''
# set1={'Bmw','Nissan','Lexus','Toyota'}
# set2={'Hummer','Lexus','Toyota','Audi',}
# set3=set1.union(set2)#Создает новый сет и то что находится в других сетах кидает в новый сет  
# print(set3)


'''17)Python Set update() Method'''
# set1={'Bmw','Nissan','Lexus','Toyota'}
# set2={'Hummer','Lexus','Toyota','Audi',}
# set1.update(set2)#Всё то что есть в сете два кидает в сет один и выводит  
# print(set1)


'''18) Write a Python program to create a set'''
# set1={'Bmw','Nissan','Lexus','Toyota'}
# print(set1)


'''19)Write a Python program to iteration over sets'''
# set1={'Bmw','Nissan','Lexus','Toyota'}
# for i in set1:
# 	print(i)


'''20)Write a Python program to add member(s) in a set'''
# set1={'Bmw','Nissan','Lexus','Toyota'}
# set1.add('Hundai')
# print(set1)


'''21)Write a Python program to remove item(s) from set'''
# set1={'Bmw','Nissan','Lexus','Toyota'}
# set1.remove('Lexus')#set1.discard() karaink oktagorceink
# print(set1)


'''22) Write a Python program to remove an item from a set if it is present in the set.'''
# set1={'Bmw','Nissan','Lexus','Toyota'}
# set1.discard('Toyota')
# print(set1)


'''23)Write a Python program to create an intersection of sets.'''
# set1={'Bmw','Nissan','Lexus','Toyota'}
# set2={'Hummer','Lexus','Toyota','Audi',}
# set3=set1.intersection(set2)
# print(set3)



'''24)Write a Python program to create a union of sets.'''
# set1={'Bmw','Nissan','Lexus','Toyota'}
# set2={'Hummer','Lexus','Toyota','Audi',}
# set3=set1.union(set2)
# print(set3)


'''25)Write a Python program to issubset and issuperset.'''
# set1={'Bmw','Nissan','Lexus','Toyota'}
# set2={'Hummer','Lexus','Toyota','Audi','Bmw','Nissan','Lexus','Toyota'}
# set3=set1.issubset(set2)#Если во втором сете нету то что есть в первом сете выводит False выводит и наоборот True
# set4=set1.issuperset(set2)#Если в первом сете есть то что есть и во втором сете выводит True  и наоборот если нету False
# print('','issubset: ',set3,'\n','issuperset: ',set4)


'''26)Write a Python program to clear a set.'''
# set1={'Bmw','Nissan','Lexus','Toyota'}
# set1.clear()
# print(set1)


'''27)Write a Python program to find maximum and the minimum value in a set.'''
# set1={10,5,8,6,3}
# max_number=sorted(set1)[-1]
# min_number=sorted(set1)[0]
# print('','max_number: ',max_number,'\n','min_number: ',min_number)


'''28)Write a Python program to find the length of a set'''
# set1={'Bmw','Nissan','Lexus','Toyota'}
# print('length set1:',len(set1))


