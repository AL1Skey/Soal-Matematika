import random
from pyperclip import copy,paste
def addtion(n,i,mns,pls):#addtion function. parameter for test value and number of test
	try:
		a,b=random.randint(mns,pls),random.randint(mns,pls)#number generator
		
		print("{}) {} + {} = ".format(str(i),str(a),str(b)))
		c=int(input())
		copy("{}) {} + {} = {} Your answer {}".format(str(i),str(a),str(b),str(a+b),str(c)))#to show answer via list
		if c==a+b:
			del a,b
			return n+1
		else:	
			del a,b
			return n
	except ValueError:
		print("Sorry,Try again...")
		addtion(n,i,mns,pls)
def substraction(n,i,mns,pls):
	try:
		a,b=random.randint(mns,pls),random.randint(mns,pls)
	
		print("{}) {} - {} = ".format(str(i),str(a),str(b)))
	
		c=int(input())

		copy("{}) {} - {} = {} Your answer {}".format(str(i),str(a),str(b),str(a-b),str(c)))#to show answer via list

		if c==a-b:
			del a,b
			return n+1
		else:
			del a,b
			return n	
	except ValueError:
		print("Sorry,Try again...")
		substraction(n,i,mns,pls)

def multiplication(n,i,mn,mx):
	try:
		a,b=random.randint(mn,mx),random.randint(mn,mx)
		print("{}) {} * {} = ".format(str(i),str(a),str(b)))
		c=int(input())

		copy("{}) {} * {} = {} Your answer {}".format(str(i),str(a),str(b),str(a*b),str(c)))#to show answer via list

		if c==a*b:
			del a,b
			return n+1
		else:
			del a,b
			return n
	except ValueError :
		print("Sorry,Try again...")
		multiplication(n,i,mn,mx)

def divide(n,i,mndiv,mxdiv,mndiv2,mxdiv2):
	try:
		while 1:
			a,b=random.randint(mndiv,mxdiv),random.randint(mndiv2,mxdiv2)
			if a%b==0:#check if true
				if a/b>random.randint(1,100):
					print("{}) {} / {} = ".format(str(i),str(a),str(b)))
					c=int(input())
					copy("{}) {} / {} = {} Your answer {}".format(str(i),str(a),str(b),str(a/b),str(c)))#to show answer via list

					if c==a/b:
						del a,b
						return n+1	
					else:
						del a,b
						return n
				else:
					del a,b
					continue
				
			else:#if false
				
				continue#continue
	except ValueError:
		
		print("Sorry,Try again...")
		divide(n,i,mndiv,mxdiv,mndiv2,mxdiv2)
'''===================================end of function========================================='''
n=0
i=1
l=[]
'''	=================================== n=0  #================================================ 
	=================================== i=1  #================================================
	=================================== l=[]#================================================ 
	=================================^ ^ ^ ^ ^ ^===============================================
									 | | | | | |
									 | | | | | |
									 n=value
									 l=list
									 i=iteration
									 *,/
									 mn=minimum
									 mx=maximum
									 +,-
									 pls=mx
									 mns=mn
									 dif=difficult                                                '''
print('''===================== Welcome to  Math dojo! =========================\n
				Choose your difficult:
				1.)Easy
				2.)Medium
				3.)Hard		''')

while 1:
	try:
		dif=int(input())
		if dif==1:
			mn,mx,mns,pls,mxdiv,mxdiv2,mndiv,mndiv2=1,10,1,100,100,10,10,1
			soal=10
		elif dif==2:
			mn,mx,mns,pls,mxdiv,mxdiv2,mndiv,mndiv2=10,500,10,1000,1000,100,100,10
			soal=20
		elif dif==3:
			mn,mx,mns,pls,mxdiv,mxdiv2,mndiv,mndiv2=10,1000,5000,100000000,10000000,100000,10000,100
			soal=30
		else:
			print("Sorry,Try again...")
			continue
		break
	except:
		continue


while 1:
	try:
		print('\n')
		arg=random.randint(1,4)#to determine which function to be called

		if arg==1:
			n=addtion(n,i,mns,pls)
			l.append(paste())
			
		elif arg==2:
			n=substraction(n,i,mns,pls)
			l.append(paste())
			
		elif arg==3:
			n=multiplication(n,i,mn,mx)
			l.append(paste())
		else:
			n=divide(n,i,mndiv,mxdiv,mndiv2,mxdiv2)
			l.append(paste())
		
		
		

		if i>=10:
			print('\n\n your score is ' , str(n),'\n\n','\n\n'.join(l))
			break

		i+=1#to increase excercise number iteration
	except ValueError:
		continue
















