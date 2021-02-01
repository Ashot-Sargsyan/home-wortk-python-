'''1)You have two list convert it in dictionary and add in (mydict.txt) and show result:'''
# import json
# def myfunction(file_name,name,estimation):
# 	classes={}
	
# 	for i,j in zip(name,estimation):
# 		classes[i]=j
	
# 	students={'Students':classes}

# 	try:
# 		file=open(file_name)
# 		return json.load(file)
# 	except FileNotFoundError:
# 		file=open(file_name,'w')
# 		json.dump(students,file,sort_keys=True)
# 		return 'File created and updated successfully'
# 	finally:
# 		file.close()

# file_name='database_students.json'
# name=['Snow','John','Will','Elizabet','Olivia','Sophia']
# estimation=[10,8,5,7,9,4]

# res=myfunction(file_name,name,estimation)
# print(res)



'''2)Create json file and save them lyrics (song) and print in cmd word this song.'''
# import json
# def myfunction(file_name,singers,text_song):
# 	artist={}

# 	for i,j in zip(singers,text_song):
# 		artist[i]=j

# 	music={'singer':artist}

# 	try:
# 		file=open(file_name)
# 		return json.load(file)
# 	except FileNotFoundError:
# 		file=open(file_name,'w')
# 		json.dump(artist,file,indent=4)
# 		return 'File created and updated successfully'
# 	finally:
# 		file.close()

# file_name='music.json'
# singers=['James Arthur ']
# text_song=['I swear to God, when I come home\n I am gonna hold you so close\n I swear to God, when I come home, I will never let go']

# res=myfunction(file_name,singers,text_song)
# print(res)



'''3)Write a python program which have one input an integer, representing the sum of all the multiples of 3 and 5 below the given input. and save this result in json file.'''
# import json
# def myfunction(file_name,number):
# 	sum_number=0

# 	for x in range(1,number+1):
# 		if x%3==0 or x%5==0:
# 			sum_number+=x

# 	return sum_number

# 	try:
# 		file=open(file_name)
# 		return json.load(file)

# 	except FileNotFoundError:
# 		file=open(file_name,'w')
# 		json.dump(sum_number,file)
# 		return'File created and updated successfully'
	
# 	finally:
# 		file.close()

# file_name='modules_number.json'
# number=int(input('Write your number if you think %3==0 and %5==0 : '))

# print(myfunction(file_name,number))


'''4)Write a program that takes in a string as input, counts and outputs the number of vowels.And add result in json file.'''

# def myfunction(file_name,word):
# 	letters={}
# 	while True:
# 		vowel='а у о ы и э я ю ё е'
# 		consonant='б в г д ж з й к л м н п р с т ф х ц ч ш щ'
# 		if word  in vowel:
# 			print('vowel word:',vowel)
# 		elif word in consonant:
# 			print('consonant word:',consonant)

# 	try:
# 		file=open(file_name)
# 		return json.load(file)
# 	except FileNotFoundError:
# 		file=open(file_name,'w')
# 		json.dump(letters,file)
# 		return'File created and updated successfully'
# 	finally:
# 		file.close()

# file_name='alphabet.json'
# word=input('write your word:')

# myfunction(file_name,word)



'''5)You have text.txt file and contains such text: Another pause and more eying and siding around each other You can create one dict where you have'''




'''6)Write a python function which get a new list from a given list, consisting of the first repeating elements.'''
# def myfunction(file_name,lists):
# 	unique_list=[]
# 	for i in lists:
# 		if i not in unique_list :
# 			unique_list.append(i)
# 	return unique_list

# 	try:
# 		file=open(file_name)
# 		return json.load(file)
# 	except FileNotFoundError:
# 		file=open(file_name,'w')
# 		json.dump(unique_list,file)
# 		return'File created and updated successfully'
# 	finally:
# 		file.close()

# file_name='list.json'
# lists=['a','b','a','b','c']

# print(myfunction(file_name,lists))


'''7)You have word.txt file and in them you have one story.Write a Python function that accepts this story and calculate the number of uppercase letters and lowercase letters. '''
