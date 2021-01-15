# '''1)We have celsius need to find a pharyngeate'''

# celsius=float(input('celsius is a :' ))
# pharyngeate=(celsius*9/5)+32
# print(pharyngeate)



# '''2)We have pharyngeate need to find a celsius'''

# pharyngeate=float(input('celsius is a :' ))
# celsius=(pharyngeate-32)*5/9
# print(celsius)




# '''3)We have 1 minute to find a second'''

# minute=float(input('minute is :' ))
# second=minute*60
# print(second)





'''4)We have 1 day and need to find a second and minute in the one day'''

# day=int(input('day is :'))
# minute=day*1440
# second=day*86400
# print( minute,'\n',second)




'''5)We have sides of a triangle'''

# a=int(input('a sides is :' ))
# b=int(input('b sides is :' ))
# result=a+b<=180
# print('the amount of glos is less',result)
# c=180-(a+b)
# result_c=c==90
# print('angle is 90 degree',c,result_c)

'''6)'''





'''7)We check our number <100 or >100'''

# number=float(input('our number : ' ) )
# result=number<=100
# print(result)

# number=float(input('our number : ' ) )
# result=number>=100
# print(result)




'''8)We check 400 modules is equal 0'''
# number=float(input('modules is :' ))
# modules=number%400==0
# print('modules is equal',modules)




'''9)We will calculate in 5 turn meter'''
# r=float(input("wheel passed meter is :" ))
# wheel=2*22/7*r
# result=5*wheel
# print(result)




'''10)We check the punctuation at the end'''

# Expression="Hi, do you check the punctuation at the end?"#endswith проверяет в конце предложение знаки препинания
# result=Expression.endswith("?")
# print(result)





# '''11)Find the desired word and convert it to a number in the sentence'''
# Sentence='Do you find the desired word,word,word,word and convert it to a number in the sentence? '
# result=Sentence.count('word')#count stringe asuma naxadasucyan mech kani ankama krknvumbare
# print(result)




'''12)You need to return any number in reverse order'''
# number1 = int(input("our number: "))
# number2 = 0
# while number1 > 0:
#     # находим остаток - последнюю цифру
#     digit = number1 % 10
#     # делим нацело - удаляем последнюю цифру
#     number1 = number1 // 10
#     # увеличиваем разрядность второго числа
#     number2 = number2 * 10
#     # добавляем очередную цифру
#     number2 = number2 + digit  
# print('return our number:', number2)



'''13)We find the right word in the right sentence'''
# word = input('write ').split()
# find = input('your word is ')
# print(word.index(find)) #index cuica tali vortexa 


'''14)We to create game a who is wants millioners'''
name=input('hello do you wants a millioners? \n Բարև ուզում ես միլիոնատեր լինել')=='yes'
print(name,'Let is go')
many=0
question1=input('How many letters of the Armenian alphabet?\n Сколько букв армянский алфавит?\n Հայերեն այբուբենի քանի տառ կա? \n a)39 b)30 c)36 d)32 ')=='a'
if question1:
	many+=500
	print(many,'dram')
else:
	print(many)
	exit()


question2=input('What year did you convert to Christianity?\n В каком году приняли христианство?\n Երբ է ընդունվել Քրիստոնեությունը?\n a)311 b)300 c)310 d)301  ')=='d' 
if question2:
	many+=1000
	print(many,'dram')
else:
	many=0
	print(many)
	exit()
question3=input('The flag of armenia consists of?\n Флаг армении состоит?\n Ինչ գույներից է բաղկացած Հայաստանի դրոշը?\n a)red, blue, orange(կարմիր, կապույտ, նարնջագույն)\n b)orange, red, blue(նարնջագույն,կարմիր, կապույտ)\n c)blue,red,orange(կապույտ,նարնջագույն,կարմիր)\n d)white,blue,red(սպիտակ,կապույտ,կարմիր)')=='a'
if question3:
	many+=2000
	print(many,'dram')
else:
	many=0
	print(many)
	exit()
question4=input('Years of the reign of King Ashot the Iron?\n Годы правления короля Ашот Железного?\n Աշոտ երկաթ արքայի գահակալությունը?\n a)915-930 b)920-935 c)914—928/929 d)913-928/929')=='c'
if question4:
	many+=3000
	print(many,'dram')
else:
	many=0
	print(many)
	exit()
question5=input('Independence day of armenia?\n Հայաստանի անկախության օրը?\n a)20 September(20 Սեպտեմբեր ) b)21 September(21 Սեպտեմբեր)\n c)22 September(22 Սեպտեմբեր) d)25 September(25 Սեպտեմբեր) ')=='b'
if question5:
	many+=5000
	print(many,'dram')
else:
	many=0
	print(many)
	exit()
question6=input('How many presidents were there in armenia?\n Քանի նախագահ կար Հայաստանում? \n a)5 b)6 c)4 d)3')=='c'
if question6:
	many+=10000
	print(many,'dram')
else:
	many=0
	print(many)
	exit()
question7=input('The main church of armenia is?\n Հայաստանի գլխավոր եկեղեցին որտեղ է?\n a)Ararat(Արարատ) b)Yerevan(Երեւան) c)Kirovakan(Կիրովական) d)Echmiadzin(Էջմիածին) ')=='d'
if question7:
	many+=15000
	print(many,'dram')
else:
	many=0
	print(many)
	exit()
question8=input('Who created the alphabet?\n Ով է ստեղծել այբուբենը?\n a)H.Tumanyan(Հ․Թումանյան) b)M.Mashtoc(Մ․Մաշտոց) c)P.Sevak(Պ․Սևակ) D)Raffi(Րաֆֆի)')=='b'
if question8:
	many+=25000
	print(many,'dram')
else:
	many=0
	print(many)
	exit()
question9=input('How old is Yerevan?\n Քանի տարեկան է Երեւանը \n a)2802 b)2800 c)2900 d)2850')=='b'
if question9:
	many+=50000
	print(many,'dram')
else:
	many=0
	print(many)
	exit()
question10=input('First partition of Armenia into two parts(between rome and persia)? \n Հայաստանի առաջին բաժանումը երկու մասի(Հռոմի և Պարսկաստանի միջև)?\n a)388 b)390 c)387 d)378 ')=='c'
if question10:
	many+=55000
	print(many,'dram')
else:
	many=0
	print(many)
	exit()
question11=input('How many states does Armenia have? \nՀայաստանը քանի նահանգ ունի?\n a)12 b)10 c)16 d)15')=='d'
if question11:
	many+=60000
	print(many,'dram')
else:
	many=0
	print(many)
	exit()



