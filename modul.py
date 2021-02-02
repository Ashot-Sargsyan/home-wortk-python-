'''1)Create a python function factorial and import this file in another file and print factorial.'''
# def factorial(n):
# 	count=1
# 	for i in range(1,n+1):
# 		count*=i
# 	return count


'''2)Write a Python function to calculate surface volume and area of a cylinder.V=πr^2h and A=2πrh+2πr^2'''
# def cylinder(height,radian):
# 	pi=22/7
# 	V=pi*radian**2*height
# 	S=2*pi*radian*(radian+height)

# 	return S,V

	
'''3)Write a Python function to calculate surface volume and area of a sphere. V = 4/3*π*r**3 and A = 4*π*r**2'''
# def surface(radius):
# 	pi=22/7
# 	V=4/3*pi*radius**3
# 	A=4*pi*radius**2

# 	return V,A


'''4)Write a Python function to convert degree to radian. one radian = pi/180: 90 radian = 1.57...'''
# def convert(degree):
# 	pi=22/7
# 	radian=degree*(pi/180)
	
# 	return radian


'''5)Write a Python function to print all primes smaller than or equal to a specified number. Call function:numbers(9) Output: (2, 3, 5, 7)'''	

def primes(number1,number2):#sarkumenq funkya
  	
	for i in range(number1, number2+1): #ciklenq sarkum vor mer i fra arachitvic minchev verchi number2+1 nshanakuma neraryal
	  if i>1:#ete i>1 
	    for j in range(2,i): #taza ciklenq sarkum vor 2 fra arten 
	        if(i % j==0): #ete i modules j == 0 
	            break#kaini
	    else: 
	        print(i)

	return i#veradarcra i