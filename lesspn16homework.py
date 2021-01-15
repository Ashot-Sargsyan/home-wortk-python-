'''1)We write a program python Dictionaries method clear'''
# thisdict={
# 	'Name':'Ashot',
# 	'last_name':'Sargsyan',
# 	'year':1996,
# 	'age':24,
# 	'phone':37498889989,
# 	'address':'Komitas',
# 	'email':'Ashot.s96@list.ru',
# 	'weight':80,
# 	'height':1.92,
# 	'month_hb':'April'
# }
# thisdict.clear()#Удаляет все элементы из словаря
# print(thisdict)



'''2)We write a program python Dictionaries method copy'''
# thisdict={
# 	'Name':'Ashot',
# 	'last_name':'Sargsyan',
# 	'year':1996,
# 	'age':24,
# 	'phone':37498889989,
# 	'address':'Komitas',
# 	'email':'Ashot.s96@list.ru',
# 	'weight':80,
# 	'height':1.92,
# 	'month_hb':'April'
# }
# newdict=thisdict.copy()#Возвращает копию словаря
# print('This is a new Dictionari:',newdict,'\n',thisdict)


'''3)We write a program python Dictionaries method fromkeys'''
# thisdict={'electrodes','gloves','pipes'}
# product=0
# thisdict=dict.fromkeys(thisdict,product)#Дает значение ключу(keys)
# print(thisdict)

'''3.1)We write a program python Dictionaries method fromkeys'''
# thisdict={'electrodes','gloves','pipes'}
# thisdict=dict.fromkeys(thisdict)#Дает значение ключу(keys)
# print(thisdict)

'''4.1)We write a program python Dictionaries method get'''
# thisdict={
# 	'model':'iphone12',
# 	'color':'green',
# 	'made':'USA',
# 	'price':810000,
# 	'currency':'AMD'
# }
# replay_value1=thisdict.get('price')#Возвращает значение цена(price) и валюта(currency) в итоге 810000 драм
# replay_value2=thisdict.get('currency')#Возвращает значение цена(price) и валюта(currency) в итоге 810000 драм
# print(replay_value1,replay_value2)


'''5)We write a program python Dictionaries method items'''
# thisdict={
# 	'model':'iphone12',
# 	'color':'green',
# 	'made':'USA',
# 	'price':810000,
# 	'currency':'AMD'
# }
# x=thisdict.items()#Возвращает список, содержащий Кортеж для каждой пары ключ-значение????
# thisdict['made']='EU'
# print(x,'\n',thisdict)


'''6)We write a program python Dictionaries method keys'''
# thisdict={
# 	'model':'iphone12',
# 	'color':'green',
# 	'made':'USA',
# 	'price':810000,
# 	'currency':'AMD'
# }
# x=thisdict.keys()
# print(x)

'''6.1)We write a program python Dictionaries method keys'''
# thisdict={
# 	'model':'iphone12',
# 	'color':'green',
# 	'made':'USA',
# 	'price':810000,
# 	'currency':'AMD'
# }
# x=thisdict.keys()#Выводим все ключи 
# thisdict['delivery']='month'#добавляем новый ключ
# print(x)


'''7)We write a program python Dictionaries method pop'''
# thisdict={
# 	'model':'iphone12',
# 	'color':'green',
# 	'made':'USA',
# 	'price':810000,
# 	'currency':'AMD'
# }

# thisdict.pop('model')#Удаляет элемент с указанным ключом
# print(thisdict)


'''8)We write a program python Dictionaries method popitem'''
# thisdict={
# 	'model':'iphone12',
# 	'color':'green',
# 	'made':'USA',
# 	'price':810000,
# 	'currency':'AMD'
# }
# thisdict.popitem()#Удаляет последнюю вставленную пару ключ-значение
# print(thisdict)


'''9)We write a program python Dictionaries method setdefault'''
# thisdict={
# 	'model':'iphone12',
# 	'color':'green',
# 	'made':'USA',
# 	'price':810000,
# 	'currency':'AMD'
# }
# x=thisdict.setdefault('made')#Ввод конкретный ключ и вывод конкретный валю(value)????
# print(x)


'''10)We write a program python Dictionaries method update'''
# thisdict={
# 	'model':'iphone12',
# 	'made':'USA',
# 	'price':810000,
# 	'currency':'AMD'
# }
# thisdict.update({'color':'green'})#Обновляет словарь с помощью указанных пар ключ-значение
# print(thisdict)

'''11)We write a program python Dictionaries method values'''
# thisdict={
# 	'model':'iphone12',
# 	'made':'USA',
# 	'price':810000,
# 	'currency':'AMD'
# }
# x=thisdict.values()#Возвращает список всех значений в словаре
# print(x)




'''12)Write a Python program to sort a dictionary by value.'''#bag unem chisht chi ashxatum menak 10 grum chi grum mecic poqr kam poqric mec
# thisdict={
# 	'number1':1,
# 	'number1':2,
# 	'number1':3,
# 	'number1':8,
# 	'number1':5,
# 	'number1':14,
# 	'number1':9,
# 	'number1':10
# }
# print(sorted(thisdict.values()))


'''13)Write a Python program to add a key to a dictionary'''

# thisdict={
# 	'model':'iphone12',
# 	'made':'USA',
# 	'price':810000,
# 	'currency':'AMD'
# }
# thisdict['color']='green'
# print(thisdict)


'''14)Write a Python program to check whether a given key already exists in a dictionary'''
# thisdict={
# 	'model':'iphone12',
# 	'made':'USA',
# 	'price':810000,
# 	'currency':'AMD'
# }
# if 'color' in thisdict:
# 	print('yes this key is there is dict')
# else:
# 	print('sorry but your key dont have is dict')


'''15)Write a Python program to merge two Python dictionaries'''
# dict1 = {'a': 50, 'b': 700}
# dict2 = {'c': 400, 'd': 600}
# dict1.update(dict2)#es sxalei grel grelei new_dict=dict1.update(dict2)
# print(dict1)


'''16)Write a Python program to multiply all the values in a dictionary.'''
# count=1#chist chem gre sxala 
# mydict = {'a':1,'b':2,'c':12}
# for i in mydict.values():#es toxe incha nshanakum?
# 	count*=i
# print(count)


# import math
# number=int(input('My naumber is :'))
# print(math.factorial(number))

