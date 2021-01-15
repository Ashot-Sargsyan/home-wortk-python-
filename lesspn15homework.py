'''1)Create new list which have 5 different data types.'''
# data_types=[15,'king',2.85,True,('car',5)]


'''2)Create new list which have data notebooks and you want check if the data have macbook?'''
# name=['Apple','Assus','Toshiba','Ph','Dell']
# notebook=input('What do you want?')
# if notebook in name:
# 	print('Very well,lets go to pay',notebook)
# else:
# 	print('Sorry your want notebooks dont have')


'''3)Password''' 
# number=0
# word=0
# symbol=0
# symbols = ('!', '@', '#', '$', '%','&','*')
# while True:
# 	password=input('Your Password is:')
# 	if len(password)>=8:
# 		for i in password:
# 			if i.isdigit():
# 				number+=1
# 			elif i.isalpha():
# 				word+=1
# 			elif i in symbols:
# 				symbol+=1
# 		if number>1 and word>1 and symbol>1:
# 			print('Your Password is strong:')
# 			break
# 		else:
# 			print('Your password uncorrect')
# 	else:
# 		print('Please write Password more reliable')


'''4)Create python program where you want to find id in link if link have id print id.'''
# link='https://www.youtube.com/watch?v=cKRRysbQZsM&feature=youtu.be'
# if '?v' in link:
# 	count=0#xienq grum count=0
# 	for i in link:
# 		count+=1
# 		if i=='=':
# 			break
# 	print(link[count:])
# else:
# 	print("error")



'''5)Create python program where you want to check if input word is palindrome or no .if yes print Open otherwise Trash'''
# word=input('Please write word: ')
# if word ==word[::-1]:
# 	print('Your word is palindrome:',word)
# else:
# 	print('your word dont palindrome')



'''6)Create python program to convert string to a list.'''
# word=input('Please write word:').split()
# print(word)


'''7)Create python program which will show all even numbers in your string. Note: you have input where have 5 numbers: '''
# numbers=[12,21,15,19,8]
# even=[i for i in numbers if i%2==0]
# print('even numbers is:',even)

'''8)Write a Python program to select the odd items of a list. And delete even items.'''
# numbers=[12,21,15,19,8]
# odd=[i for i in numbers if i%2==1]
# del numbers[3]
# print(numbers,'\n','odd numbers is:',odd)

'''9)Your group have 5 people and each of them can take one name and when take this name is delete from this list.And he can not take his name:'''
# import random
# x=['Ani','Ash','Raz','Gag','Nver']
# for i in range(5):
# 	print(x)
# 	name=random.choice(x)
# 	print(name)
# 	x.remove(name)


'''10)Create a python program which delete all duplicate items in list'''
# list1=[12,20,36]
# list2=[12,20,36]
# for i in list1:
# 	if i in list2:
# 		list2.remove(i)
# print(list2,list1)

# c=[]
# x=[1,2,3,4,5,6,8,4]
# for i in x:
# 	if i not in c:
# 		c.append(i)
# print(c)

		