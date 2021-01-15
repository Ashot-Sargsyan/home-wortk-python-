'''1)Create new dictionary where you have 10 students and each of them have rating(1-10).'''
# students={
# 	'Donald':4,
# 	'Walter':8,
# 	'Oliver':9,
# 	'Benjamin':8.5,
# 	'Logan':5,
# 	'Snow':9,
# 	'Anabel':8,
# 	'Elizabet':9,
# 	'Olivia':6,
# 	'Emma':7
# }
# print(students)



'''2)Create python program which will calculate the arithmetic average of rating students'''
# students={
# 	'Sophia':9,
# 	'Izabella':7,
# 	'Charlotte':8,
# 	'Liam':8,
# 	'William':7,
# 	'James':5
# }

# count=0

# for i in students.values():
# 	count+=i
# result=count/len(students)

# print('The arithmetic average of rating students : ',result)


'''3)Create a python program which will say you who they are good and bad students.'''
# students={
# 	'Lucas':9,
# 	'Abigail':8,
# 	'Ella':6,
# 	'Alexander':10,
# 	'Scarlett':9,
# 	'Henry':7,
# 	'Penelope':5,
# 	'Jacob':5
# }
# max_Reding=sorted(students.values())[-1]
# min_Reding=sorted(students.values())[0]
# for i in students:
# 	if students[i]==max_Reding:
# 		print('The best estimate : ',i,max_Reding)
# 	elif students[i]==min_Reding:
# 		print('The worst estimate : ',i,min_Reding)


'''4...5)Bad and Good students'''
# students={
# 	'Lucas':9,
# 	'Abigail':8,
# 	'Ella':6,
# 	'Alexander':10,
# 	'Scarlett':9,
# 	'Henry':7,
# 	'Penelope':5,
# 	'Jacob':5
# }
# for i in students:
# 	if students[i]<=5:
# 		print('students who did not succeed academically : ',i)
# 	elif students[i]>8:
# 		print('students who Excel academically : ',i)		


'''6)Create a python program which will say if your dictionary have this name print name and raiting'''
# students={
# 	'Lucas':9,
# 	'Abigail':8,
# 	'Ella':6,
# 	'Alexander':10,
# 	'Scarlett':9,
# 	'Henry':7,
# 	'Penelope':5,
# 	'Jacob':5
# }
# name=input('Write name students : ')
# if name in students:
# 	print('your student is on the list ։ ',name)
# else:
# 	print('your student is not on the list')


'''7)Create a new dictionary:For example…'''
# s = 'a,2,b,5,c,8,a,4,e,11'.split(',')
# c={}
# for i in range(0,len(s),2):
# 	if s[i] in c:
# 		c[s[i]]=int(s[i+1])+int(c[s[i]])
# 	else:
# 		c[s[i]]=s[i+1]
# print(c)


'''7.1)Create a new dictionary:For example…'''
# s = 'a,2,b,5,c,8,a,4,e,11'.split(",")
# myDict={}
# num = []
# letter=[]
# for i in s:
# 	if i.isalpha():
# 		letter.append(i)
# 	else:
# 		num.append(i)
# n=0		
# for i in letter:
# 	if i in myDict:
# 		myDict[i] = int(myDict[i]) + int(num[n])
# 	else:	
# 		myDict[i]=int(num[n])
# 	n+=1

# print(myDict)


'''8)Create a dictionary from a string.Track the count of the letters from the string'''
# word = 'exercises'
# c={}
# for i in word:
# 	if i in c:
# 		c[i]=c[i]+1
# 	else:
# 		c[i]=1
# print(c)


'''9)Create a python game Millionaire.'''
# print('Welcome to the game who wants to be a millionaire')
# print('Rule of the game:You answer 15 questions and earn money every time')
# while True:
# 	money=0
	
# 	questions1=input('What year did you convert to Christianity? \n a)311 b)300 c)310 d)301 ' ) == 'd'
	
# 	if questions1 :
# 		money+=500
# 		print('congratulations you answered correctly','\n',money,'AMD')
		
# 	else:
# 		print('Sorry but you lose. \n Try again:')


# 	questions2=input('How many letters of the Armenian alphabet? \n a)39 b)30 c)36 d)32 ' ) == 'a'
	
# 	if questions2:
# 		money+=500
# 		print('congratulations you answered correctly','\n',money,'AMD')
		
# 	else:
# 		print('Sorry but you lose. \n Try again:')

# 	questions3=input('Independence day of armenia? \n a)20 September(20 Սեպտեմբեր ) b)21 September(21 Սեպտեմբեր)\n c)22 September(22 Սեպտեմբեր) d)25 September(25 Սեպտեմբեր) ' ) == 'b'
	
# 	if questions3:
# 		money+=500
# 		print('congratulations you answered correctly','\n',money,'AMD')
# 	else:
# 		print('Sorry but you lose. \n Try again:')

# 	questions4=input('How many presidents were there in armenia? \n a)5 b)6 c)4 d)3 ' ) == 'c'

# 	if questions4:
# 		money+=500
# 		print('congratulations you answered correctly','\n',money,'AMD')
# 	else:
# 		print('Sorry but you lose. \n Try again:')

# 	questions5=input('The main church of armenia is? \n a)Ararat(Արարատ) b)Yerevan(Երեւան) c)Kirovakan(Կիրովական) d)Echmiadzin(Էջմիածին) ' ) == 'd'

# 	if questions5:
# 		money+=500
# 		print('congratulations you answered correctly','\n',money,'AMD')
# 	else:
# 		print('Sorry but you lose. \n Try again:')

# 	questions6=input('Who created the alphabet? \n a)H.Tumanyan(Հ․Թումանյան) b)M.Mashtoc(Մ․Մաշտոց) c)P.Sevak(Պ․Սևակ) D)Raffi(Րաֆֆի) ' ) == 'b'
# 	if questions6:
# 		money+=500
# 		print('congratulations you answered correctly','\n',money,'AMD')
# 		break
# 	else:
# 		print('Sorry but you lose.')
# 		break
