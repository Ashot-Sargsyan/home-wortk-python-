# def my_function():
# 	print('hello i am function')
# my_function()

# def my_function(first_name,last_name):
# 	print('','first_name:',first_name,'\n','last_name:',last_name)
# my_function('Dinul','Sargsyan')

# def my_function(child1,child2):
# 	print('the yongest  child:',child1)
# my_function('John','Nick')

# def my_function(x):
# 	print('max number is :',max(x))
# list1=[12,5,6,7,8,-2.56]
# my_function(list1)


# def my_function(x):
# 	print('sum number:',x)
# count=0
# list1=[12,50,6,9]
# for i in list1:
# 	count+=i
# 	# print(count)
# my_function(count)


# def my_function(user,user1,user2,user3):
# 	print('your name is : ',user,age,years,work)
# name=input('please write your name: ')
# age=int(input('your age is : '))
# years=int(input('your years is :'))
# work=input('do you work or no ')
# my_function(name,age,years,work)


'''1)calculator'''
# def add(x,y):
#  return(x+y)

# def subtract(x,y):
#  return(x-y)

# def divide(x,y):
#  return(x/y)

# def multiply(x,y):
#  return(x*y)

# def result(choice,x,y):
 
#  if choice == '+':
#   print(add(x,y))
#  elif choice == '-':
#   print(subtract(x,y))
#  elif choice == '/':
#   print(divide(x,y))
#  elif choice == '*':
#   print(multiply(x,y))
 
# choice=input('choice ...')
# x=int(input('x = '))  

# while True:
#  y = int(input('y: '))
#  if choice =='/': 
#   if y != 0:
#    result(choice,x,y)
#    break
#   else:
#    print('please not 0') 
#  else:
#   result(choice,x,y) 
#   break


'''2)Write a python program  to find max of two numbers'''
# def my_function(x):
# 	print('max number:',max(x))
# list1=[10,19]
# my_function(list1)


'''3)Write a python program to sum all numbers'''
# def my_function(sum_numbers):
# 	print('sum all numbers:',sum_numbers)
# count=0
# list1=[12,10,5,8,7,6,3]
# for i in list1:
# 	count+=i
# my_function(count)


'''4)Write a python program to multiply all numbers'''
# def my_function(multiply_numbers):
# 	print('multiply all numbers:',multiply_numbers)
# count=1
# list1=[1,5,6,8,10]
# for i in list1:
# 	count*=i
# my_function(count)


'''5)Write a python program to sum all letter and number in your string'''
# def my_function(x):
# 	print('all letter and number',x)
# tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e','s','15','80','as863')
# mystr = ''.join(tup)
# my_function(mystr)


# def my_function(word):
# 	letter=0
# 	number=0
# 	for i in word:
# 		if i.isalpha():
# 			letter+=1
# 		elif i.isdigit():
# 			number+=1
# 	return letter,number
# string=(' ')#es pahe chem jogum ete grei string =('hello') ban chi anum xi 
# print(my_function('wordadsfd121223384'))


'''6)You are given a program that takes all 3 passengers ages as inputs and inserts them in a list'''
# passengers1=int(input('passengers1 = '))
# passengers2=int(input('passengers2 = '))
# passengers3=int(input('passengers3 = '))
# def myfunction(age1,age2,age3):
# 	print('','age1 = ',age1,'\n','age2 = ',age2,'\n','age3 = ',age3)
# if passengers1<=16 or passengers2<=16 or passengers3<=16:
# 	print('your age doesnt match')
# elif not(passengers1<16 or passengers2<16 or passengers3<16):
# 	print('lets go')
# myfunction(passengers1,passengers2,passengers3)