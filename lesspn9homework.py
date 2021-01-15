'''1)We write a program python compare two numbers'''
# import random
# siri=random.randint(0,100)
# human=int(input('human number:'))
# if human==siri:
# 	print('Error')
# elif human<siri:
# 	print('siri is a big')
# elif human>siri:
# 	print('human is a big')


'''2)We write a program python compare 3 people who are older who are younger'''

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



'''3)We write a program python inverse number'''

# number=input('')
# print(number[::-1],'number')


'''4)We write a program python work only in urban areas or only in urban areas '''

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




'''5)Rock, Paper, Scissors'''

# import random
# point=0
# while True:
# 	game='rps'
# 	siri=random.choice(game)#choise stringi mechic randommi ban vekaluma
# 	ash = input('rps')
# 	if siri == 'r' and ash=='p' or siri=='p' and ash=='s' or siri=='s' and ash=='r' :
# 		point+=1
# 		print('Ashot the win',point)
# 		break
# 	elif not(siri == 'r' and ash=='p' or siri=='p' and ash=='s' or siri=='s' and ash=='r' ):
# 		point+=1
# 		print('siri the win',point)
# 		break



'''6)Instagram(bloger)'''

# import random
# siri=random.randint(1,100)
# Ashot=int(input('Ashot Followers:'))
# if Ashot<=siri :
# 	print('Siri is a bloger')

# elif Ashot+Ashot*0.2<siri:
# 	print('Siri is a bloger')
# elif Ashot+Ashot*0.2>siri:
# 	print('Ashot is a bloger')
# else:
# 	print('Error')


'''7)Rally'''
s=12
siri_t=3
result_siri_v=s/siri_t
human_t=siri_t/60
print('siri v:',result_siri_v,'\n','human time:',human_t)
res=result_siri_v-0.05
print('',res)
