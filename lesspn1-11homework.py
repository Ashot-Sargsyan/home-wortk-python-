# '''1)We writen a program python where input() to print Hello (your name) , I am (your age) years old. '''
# name=input('Hello,my name is:')
# age=input('My age is:')
# print('Hello,your name is:',name,'\n','your age is:',age)

'''2)Write a python program which have two input and compute the area of a rectangle.'''
# a=float(input('first side:'))
# b=float(input('secon side:'))
# result=a*b>0
# print('S rectangle is :',result)

'''3)Write a python program which have one input and compute the area of a square.'''
# a=float(input('first side:'))
# result=a**2
# print('S square is :',result)

'''4)Create  legal variables.'''
# it='programing'
# print(it)
# print(type(it))

# programing="python"
# print(programing)
# print(type(programing))

# age='2020'
# print(age)
# print(type(age))


# age=1998
# print(age)
# print(type(age))

# number="not word"
# print(number)
# print(type(number))


# siri='this is computer'
# print(siri)
# print(type(siri))


# year=1248
# print(year)
# print(type(year))


# construction='magazine'
# print(construction)
# print(type(construction))

# fittings=10
# print(fittings)
# print(type(fittings))



'''5)Write code to print pypypypython'''
# word1='py'
# word2='thon'
# result=word1*3+word2
# print(result)


'''6)Write code to print 7p7p7p79'''
# word1='7p'
# number='79'
# result=word1*3+number
# print(result)



'''7)Write code to print 9999999'''
# number='9'
# result=number*7
# print(result)



'''8)Write a Python program that checks how much money you have on your card.'''
# Visacard=0
# entrance1=int(input('amd:'))
# result1=entrance1+Visacard
# entrance2=int(input('amd:'))
# result2=entrance2+Visacard
# entrance3=int(input('amd:'))
# result3=entrance3+Visacard
# res=result1+result2+result3
# print('entrance amd:',res)


'''9)how much fahrenheit is your Celsius.'''
# fahrenheit=float(input('fahrenheit:'))
# Celsius=(fahrenheit-32)*5/9
# print('Celsius:',Celsius)



'''10)how much Celsius is your Fahrenheit.'''
# Celsius=float(input('Celsius:'))
# Fahrenheit=(Celsius*(5/9))+32
# print('Fahrenheit',Fahrenheit)



'''11)Convert Minutes into Seconds you have one input.'''
# Minutes=int(input('Minutes:'))
# Seconds=Minutes*60
# print('Seconds:',Seconds)



'''12)Convert Day into Minutes and Seconds you have one input. '''
# Day=int(input('Day:'))
# Minutes=Day*(24*60)
# Seconds=Minutes*60
# print('Minutes:',Minutes,type(Minutes),'\n','Seconds',Seconds,type(Seconds))


'''13)you will check that triangle have 90 degree angle.'''
# a=float(input('first side: ' ))
# b=float(input('second side: ' ))
# res_c=a+b<=180
# c=180-(a+b)
# print('first and second side:',res_c,'\n','three side:',c)



'''14)We check our number <100 or >100'''
# number=float(input('number:'))
# result=number>100 or number<100
# print('number:',result)



'''15)check,if modulo 400 is 0 True, otherwise False'''
# number=int(input('number:'))
# result=number%400==0
# print('number :',result)



'''16)You have a wheel: calculate how much meter it will pass after 5 turn.'''
# r=float(input("wheel passed meter is :" ))
# wheel=2*22/7*r
# result=5*wheel
# print(result)



'''17)We check human number (1,10) random siri'''
# import random
# siri=random.randint(1,10)
# human=int(input('human number:'))
# result=human==siri
# print('number:',result,siri)



'''18)We check  human number (10,100)  is big or small number siri'''
# import random
# siri=random.randint(10,100)
# human=int(input('human number:'))
# result1=human>siri
# result2=human<siri
# print('number:',siri,result1,result2)



'''19)My birthday is calendary'''
# import calendar
# year=int(input('My year is :'))
# month=int(input('My month is:'))
# day=int(input('My day is :'))
# print(calendar.month(year,month,day))




'''20)We write to Discriminate(6*x**2+10*x-1=0)'''
# import math
# import time
# a=6
# b=10
# c=1
# Discriminate=b**2-4*a*c
# print(Discriminate)
# x1=-b+math.sqrt(Discriminate)/(2*a)
# x2=-b-math.sqrt(Discriminate)/(2*a)
# time.sleep(5)
# print('Our Discriminate :',Discriminate,x1,x2)



'''21)We have a radius circle'''
# import math
# import random
# random=random.randint(0,10)
# r=2*math.pi*2*random**2
# print(random,r)




'''22) Write a python program to check have your name ‘a’ or no.You have 2 input.'''
# name='Ashot'
# print('A' in name)

'''23)Write a python program to check have your number ‘7’ or no.You have 2 input.'''
# number='116265461983'
# print('7' not in number)

'''24)We writen a program to check if there  are bananas, oranges and apples in your fridge'''
# bananas =input('Have you banana in fridge:') == 'yes'
# print('I have banana',bananas)
# oranges =input('Have you oranges in fridge:') == 'yes'
# print('I have oranges',oranges)
# apples =input('Have you apples in fridge:') == 'yes'
# print('I have apples',apples)

'''25)We write to a program check the following conditions'''
# import random
# x=random.randint(-8,15)
# result=x<=-8 or x>12
# print('my x =',x,'\n',result)

# y=random.randint(10,50)
# result=y>10 or y==50
# print('my y =',y,'\n',result)

# z=random.randint(-9,11)
# result=z>-10 or z<10
# print('my z =',z,'\n',result)

# t=random.randint(20,50)
# result=t!=20 or t>50
# print('my t =',t,'\n',result)

'''26)We write a program is there any fruit in the refrigerator if not then you need to buy it'''
# bananas =input('Have you banana in fridge:') == 'yes'
# print('I have banana',bananas)
# print('buy bananas in magazine', not bananas)
# oranges =input('Have you oranges in fridge:') == 'yes'
# print('I have oranges',oranges)
# print('buy oranges in magazine',oranges)
# apples =input('Have you apples in fridge:') == 'yes'
# print('I have apples',apples)
# print('buy apples in magazine',not apples)
# light=input('Have you light at home?' ) == 'yes'
# print(light)
# res_bananas=bananas and not light
# print('Get banana in fridge:',res_bananas)
# res_oranges=oranges and light
# print('Get oranges in fridge:',res_oranges)
# res_apples=apples and not light
# print('Get apples in fridge:',res_apples)

'''27)'''
# language=input('What language do you speak?')
# language=language.upper()#sax mecasnuma
# print('I speak language a',language)



'''28)'''
# language=input('What language do you speak?')
# language=language.capitalize()#Arachin tare mecasnuma
# print('I speak language a',language)


'''29)We write a program where we buy to a phone'''
# phone=input('do have you apple or samsung')=='yes'
# model=input('do  have a iphone 12 pro max ')=='yes'
# iphone = phone and model
# if iphone:
# 	print('i wanted to buy iphone 12 pro max black ')
# else:
# 	print('sorry, do you wanted samsung galaxsy 11')



'''30)We writen a program where a chek 5  question'''
# question1=input('Where you were born')=='Russia'
# question2=input('Where are you living now')== 'Armenia'
# question3=int(input('How old do you live in Armenia'))==15
# question4=input('Do you study')=='yes'
# question5=input('Do you a work')== 'yes'
# result=question1 and question2 and question3 and question5 or question4
# if result:
# 	print('very well,you can workour office')
# else:
# 	print('sorry,but you dont work uor office')


'''31)We writen a program where cheak age employee'''
# import random
# age=random.randint(17,25)
# result_age = 17<=age<=25
# print(age,result_age)
# higher_education=input('do you have higher_education? ')=='yes'
# work=input('do you experience?')=='yes'
# human=result_age and work or higher_education
# if human:
# 	print('Very well','\n','your age is :',age,'\n','you fit in our age in company:',result_age,'\n','your higher_education',higher_education,'\n','your experience is  not bad',work)
# else:
# 	print('you didnt enter work our office')

'''32)Dream car'''
# cars='BMW toyota hundai kia lada mercedes'
# company=input('we have many cars')
# if company in cars:
# 	print('very well,lets go to buy')
# else:
# 	print('your dream car dont buy in  our company ')


'''33)We write a program math (a+b)**3'''
# a=5
# b=6
# x=(a+b)**3
# print(x)

# x=a**3+3*a**2*b+3*a*b**2+b**3
# print(x)


'''34)Use random module if find'''
# import random
# siri=random.randint(1,10)
# human='1 10 5 4 8 3 7'
# result=str(siri) in human
# if result:
# 	print('my number is :',human ,'\n','number siri is :',siri,'\n',result,)
# else:
# 	print('your number is FALSE',siri)

	
'''35)Factorial'''
# import math
# number=int(input('My naumber is :'))
# print(math.factorial(number))


'''36)Write a Python program to calculate a dog's age in human years.'''
# dog_year=int(input('dogs year is:'))
# if dog_year<0:
# 	print('error')
# elif dog_year<3 and dog_year>0:#так как после 4 лет год собаки идет на 2
#  	print('human years is:',dog_year*5.25) #1 до 3 лет узнаем сколько лет собаке по человеческим меркам

# else:
# 	res = 10.5 + (dog_year-2) * 4 #с 4 лет и после узнаем сколько лет собаке по человеческим меркам
# 	print('human age is',res)



'''37)Write program a python to check whether an alphabet is a vowel or consonant.'''
# letters=input('')
# vowel='а у о ы и э я ю ё е'
# consonant='б в г д ж з й к л м н п р с т ф х ц ч ш щ'
# if letters in vowel:
# 	print('vowel letters',vowel)
# elif letters in consonant:
# 	print('consonant letters',consonant)
# else:
# 	print('Error')



'''38)Write a Python program to check this year is leap year or no.'''
# year=int(input('year is :'))
# if year%4 or year%100 and year%400:
# 	print('leap year',year)
# else:
# 	print('Error')



'''39)Write a Python program to check if your number is odd or even'''
# number=float(input('Our number check is even'))
# if number/2:
# 	print('number is even')
# else:
# 	print('number is odd')


'''40)Write a python program which will say who win in game.'''
# import random
# pc=random.randint(0,5)
# human=int(input('number human:'))
# human_point=0
# pc_point=0
# while True:
# 	if pc>human:
# 		pc_point+=1
# 		print('pc the win ', pc_point)
# 		break
# 	elif human>pc:
# 		human_point+=1
# 		print('human the win',human_point)
# 		break
# 	else:
# 		print('Error')


'''41)Take two int values from user and print greatest among them.'''
# import random
# number1=random.randint(1,100)
# number2=int(input('number2 :'))
# number1_point=0
# number2_point=0
# while True:
# 	if number1>number2:
# 		number1_point+=1
# 		print('number1 is big',number1,number1_point)
# 		break
# 	elif number1<number2:
# 		number2_point+=1
# 		print('number2 is big',number2,number2_point)
# 		break
# 	else:
# 		print('Error')


'''42)We write a program python compare 3 people who are older who are younger'''

# John=float(input('John:'))
# Nick=float(input('Nick:'))
# Elizabet=float(input('Elizabet:'))
# if John==Nick and John==Elizabet or John<0 or Nick<0 or Elizabet<0:
# 	print('Error,please write age corect')
# elif John>Nick and John>Elizabet and Nick>Elizabet:
# 	print('John is a older and Elizabet is a younger')
# elif John>Nick and John>Elizabet and Nick<Elizabet:
# 	print('John is a older and Nick is a younger')
# elif Nick>John and Nick>Elizabet and John>Elizabet:
# 	print('Nick is a older and Elizabet is a younger')
# elif Nick>John and Nick>Elizabet and John<Elizabet:
# 	print('Nick is a older and John is a younger')
# elif Elizabet>Nick and Elizabet>John and Nick>John:
# 	print('Elizabet is a older and John is a younger')
# elif Elizabet>Nick and Elizabet>John and Nick<John:
# 	print('Elizabet is a older and Nick is a younger')


'''43)We write a program python inverse number'''

# number=input('')
# print(number[::-1],'number')

'''44)We write a program python work only in urban areas or only in urban areas'''

# floor=input('male of female? ')
# age=int(input('your age, please: '))
# marital_status=input('married or celibate: ')
# if floor=='female':
# 	print('you work only in urban areas')
# elif floor=='male'and age>0 and 20<=age<=40:
# 	print('you may work in anywhere')
# elif floor=='male' and 40<=age<=60:
# 	print('you work in urban areas only.')
# else:
# 	print('Error')


'''45)Rock, Paper, Scissors'''#ktelem bag aysiqn pc = userin baic tpuma vor usere krele
# import random
# while True:
# 	game='rpc'
# 	point=0
# 	pc=random.choice('rpc')
# 	user=input('rps')
# 	if pc=='r' and user=='s' or pc=='p' and user=='r' or pc=='s' and user=='p':
# 		print('pc is the win',user, pc)
# 		point+=1
# 		break
# 	elif not(pc=='r' and user=='s' or pc=='p' and user=='r' or pc=='s' and user=='p'):
# 		print('user is the win',user, pc)
# 		point+=1
# 		break
# 	else:
# 		print('Error')

'''46)Instagram'''
# import random
# pc=random.randint(1,100)
# user=int(input('user Followers:'))

# if user<=pc :
# 	print('pc is a bloger')

# elif user+user*0.2<pc:
# 	print('pc is a bloger')

# elif user+user*0.2>pc:
# 	print('user is a bloger')

# else:
# 	print('Error')


'''47)We writen programa python when we check number siri equal human'''
# import random
# while True:
# 	pc=random.randint(1,20)
# 	count=0
# 	user=int(input('user number:'))
# 	if user<=0 or user>=21:
# 		print('please writen number (1,20)',user,pc)
# 	elif user==pc:
# 		print('user number and number siri is equal',user,pc)
# 		count+=1
# 		break
# 	elif user!=pc:
# 		print('user number and number siri is dont equal',user,pc)
# 		count+=1
# 		break
# 	else:
# 		print('Error')


'''48) Number of even and odd'''
# import random
# number=random.randint(1,100)
# while True:	
# 	if number<=0:
# 		print('please writen number (1,100)')
# 		break
# 	elif number%2:
# 		print('number is odd:',number)
# 		break
# 	elif not(number%2):
# 		print('number is even:',number)
# 		break
# else:
# 	print('you uncorect number')


'''49)Fibonacci'''
# x,y=0,1#fibonachi chisht chi asxatum minvhev 34
# print(0)
# while y<=40:
# 	print(y)
# 	x,y=y,x+y


'''50)Letters and numbers'''
# tarer= 0
# tver = 0
# probel = 0
# keter  = 0
# word=input('---  ')
# for i in word:
# 	if i.isalpha():
# 		tarer += 1
# 	elif i.isdigit():
# 		tver += 1
# 	elif i == " ":
# 		probel+=1
# 	elif i ==".":
# 		keter+=1 
# print(tarer,tver,probel,keter)



'''51)Write a Python program which have number (73421):You should calculate (7 + 3 + 4 ….):'''
# count = 0#counte patasxana havasara 0
# number=int(input(''))
# for i in str(number):#str integere darcnuma string vor fra meche
# 	count += int(i)#gumarumem i aysiqn stringi mechi gracnere gumarumem irar
# print(count)


'''52)Factorial'''

