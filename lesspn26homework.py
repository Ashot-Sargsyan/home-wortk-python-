'''1). Write a Python program to add info in JSON file about you.'''

# import json
# file_name='database_me.json'
# people={
# 	'name':'John',
# 	'age':23,
# 	'country':'Yerevan',
# 	'hight':192,
# 	'weight':80,
# 	'work_now':'Yes'
# }
# diction=[people]
# with open(file_name,'w') as  file:
# 	json.dump(diction,file)

'''2)Write a Python program to get info in JSON file about you.'''
# file=open(file_name)
# json_database=json.load(file)
# for x in json_database:
# 	print('cikl: ',x)


'''3)Write a Python program to check if your json file have this info.'''
# try:
# 	file=open(file_name)
# 	print( json.load(file))
# except FileNotFoundError:
# 	file=open(file_name,'w')
# 	json.dump(file)
# 	print('File created and updated successfully')
# finally:
# 	file.close()	