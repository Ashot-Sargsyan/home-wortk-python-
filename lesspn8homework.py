'''1)We writen a program python if,elif,else'''
# import random
# while True:
# 	a=random.randint(0,20)
# 	b=14
# 	if a>b:
# 		print('a is big b')
# 	elif a<b:
# 		print('a is smol b')
# 	else:
# 		print('your request is incorrect')
# 		break



'''2)We writen a program python data logging(rezume)'''
# human=input('Ashot Sargsyan')
# higher_secondary=input('Do you have higher secondary?')
# age=input('Your age must be >=21')
# full_name=input('Your full name')

# if human in higher_secondary and age and full_name :
# 	print('Very well,you are accepted',higher_secondary,age,full_name)
# else:
# 	print('Sorry,you didnt are accepted')



'''3)We writen a program python calculate dog live in human '''
# dog_age=int(input('Dogs age is :'))
# if dog_age<=0:
#  	print('its unposible')
# elif dog_age>=2 and dog_age>0:
#  	print('Your dogage is:',dog_age*5,25)


'''4)We write a program python check whether an alphabet is a vowel or consonant'''
# letters=input('')
# vowel='а у о ы и э я ю ё е'
# consonant='б в г д ж з й к л м н п р с т ф х ц ч ш щ'
# if letters in vowel  :
# 	print('vowel letters',vowel)
# elif letters in consonant:
# 	print('consonant letters',consonant)
# else:
# 	print('please enter the correct information')

'''5)We writen a program where a check in year leap or no'''
# years=float(input('Year leap'))
# if years%100 and years%400:
# 	print('yes years is leap')
# else:
# 	print('no years is no leap')
	



'''6)We writen a program python where check number is odd or even'''
# number_phone=float(input('Our number check is even'))
# if number_phone/2:
# 	print('number is even')
# else:
# 	print('number is odd')


'''7)We writen a program  python in game human and siri'''
# import random
# siri=random.randint(0,5)
# human=int(input(''))
# human_point=0
# siri_point=0
# if siri>human:
# 	siri_point+=1
# 	print('siri is win ', siri_point)
# elif siri<human:
# 	human_point+=1
# 	print('human is win ',human_point)

# else:
# 	print('human equal siri ')



'''8)We write a program python real calculate'''


import math
number1=(input('number first:' ))
if number1.isdigit() :
	print('your input is correct',number1)
else:
	print('your input is uncorrect')
	exit()
number2=(input('number two:' ))
if number2.isdigit() :
	print('your input is correct',number2)
else:
	print('your input is uncorrect')
	exit()
choice=input('+ - * / ')
if choice=='+':
	print('our number is equa',number1+number2)
elif choice=='-':
	print('our number is equa',number1-number2)
elif choice=='*':
	print('our number is equa',number1*number2)
elif choice=='/':
	print('our number is equa',number1/number2)
else:
	print('Error')









