'''1.0)Create 5 file (.txt) and write messages in them'''
# f=open('database.txt','r')
# print(f.read())


'''1.1)Create 5 file (.txt) and write messages in them'''
# f=open('database1.txt','r')
# print(f.read())


'''1.2)Create 5 file (.txt) and write messages in them'''
# f=open('database2.txt','r')
# print(f.read())


'''1.3)Create 5 file (.txt) and write messages in them'''
# f=open('database3.txt','r')
# print(f.read())


'''1.4)Create 5 file (.txt) and write messages in them'''
# f=open('database4.txt','r')
# print(f.read())


'''2)Write a Python program to read first n lines of a file.'''
# f=open('database.txt','r')
# number_of_lines = int(input('what line do you need? '))
# for i in range(number_of_lines):
# 	i = f.readline()
# 	print(i)


'''3)Write a Python program to append text to a file and display the text.'''
# def new_file(file,mode,text):
	# try:
	# 	f=open(file,mode)
	# 	print(f.read())
	# except FileNotFoundError:
	# 	f=open(file,'w')
	# 	f.write(text)

# file='database5.txt'
# mode='r'
# text='\t I understood everything \n most likely I didnt understand anything'
# new_file(file,mode,text)


'''4)Write a python program to find the longest words.'''

# a=['hello','sum','goodbuy','please']
# res=[i for i in a if len(i)==max([len(i) for i in a])]
# print(' '.join(res))

'''5)Write a python program to find numbers in txt.'''
# f=open('database1.txt')
# for x in f:
# 	for i in x:
# 		if i.isdigit():
# 			print(i)


'''6)Write a python program to get login and password.'''
# with open('password.txt','w') as f:
# 	login = input('write your login: ')
# 	password = input('write your password: ')
# 	a='login'+login+' '+'password'+password
# 	f.write(a)

# with open('password.txt') as f:
# 	print(f.read())



file=open('database7.txt','w')
file.write('i write this line\n')

file=open('database7.txt','a')
file.write('king only ')