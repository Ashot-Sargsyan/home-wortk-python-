'''Exception Handling'''

'''1)IndexError is thrown when trying to access an item at an invalid index.(set,list,tuple,dictionary ) '''

# my_list=[15,9,5,7,0,3]

# try :
# 	print(my_list[6])

# except IndexError:
# 	print('An error occurred while trying to access an element with an invalid index').



'''2)KeyError is thrown when a key is not found.'''

# my_dictionary={
# 	'python':'program',
# 	'user':'human',
# }
# try:
# 	print(my_dictionary['C#'])
# except KeyError:
# 	print('please write the key that we have ')


'''3)TypeError is thrown when an operation or function is applied to an object of an inappropriate type.'''

# my_dictionary={
# 	'python',
# 	'user'
# }
# try:
# 	print(my_dictionary['python'])
# except TypeError:
# 	print('Your type is wrong, please cheak')


'''4)NameError is thrown when an object could not be found.'''
# try:
# 	print(user)
# except NameError:
# 	print('please cheak your name ')


'''5)ZeroDivisionError is thrown when the second operator in the division is zero.'''
	
# number1=int(input('number1: '))
# number2=0
# try:	
# 	res=number1/number2
# 	print(res)
# except ZeroDivisionError:
# 	print('you cant divide a number by zero')


'''6)ModuleNotFoundError is thrown when a module could not be found.'''
# try:
# 	import jhgdajkhl
# except ModuleNotFoundError:
# 	print('We dont have this name import, please cheak your write import')


'''7)Password generator with try except.'''
# try:
# 	import random
# except ModuleNotFoundError:

# 	print('We dont have this name import, please cheak your write import')
# def my_function():
# 	password=''
# 	letters='ahgdifhwouigcjasq'
# 	numbers='753198246012687'
# 	choice='!@#$%^&*()+-*/><:'

# 	letters_count=6
# 	numbers_count=choice_count=3
# 	for i in range(letters_count):
# 		l=random.choice(letters)
# 		password+=l
	
# 	for i in range(numbers_count):
# 		n=random.choice(numbers)
# 		c=random.choice(choice)
# 		password+=n
# 		password+=c

# 	password=list(password)
# 	random.shuffle(password)
# 	return''.join(password)
# print(my_function())






'''8)Calculator'''
def add(x,y):
 return(x+y)

def subtract(x,y):
 return(x-y)

def divide(x,y):
 return(x/y)

def multiply(x,y):
 return(x*y)

def result(choice,x,y):
 
 if choice == '+':
  print(add(x,y))
 elif choice == '-':
  print(subtract(x,y))
 elif choice == '/':
  print(divide(x,y))
 elif choice == '*':
  print(multiply(x,y))
try: 
	choice=input('choice : ')
except KeyboardInterrupt:
	print('\nyou stopped the program')
try:
	x=int(input('x = '))  
except ValueError:
	print('Duq karoxek menaq tiv mutk anel')
except KeyboardInterrupt:
	print('\nyou stopped the program')

try:
	while True:
	 
	 y = int(input('y = '))
	 if choice =='/': 
	  if y != 0:
	   result(choice,x,y)
	   break
	  else:
	   print('please not 0') 
	 else:
	  result(choice,x,y) 
	  break

except ValueError:
	print('Duq karoxek menaq tiv mutk anel')
except KeyboardInterrupt:
	print('\nyou stopped the program')

except ZeroDivisionError:
	print('you cant divide a number by zero')

