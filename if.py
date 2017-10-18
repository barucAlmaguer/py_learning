greeting = True

if greeting :
	print("hi!")
else :
	print("bye")


#ejecutar con py -i <filename> para
#llamar funciones interactivamente desde consola
def sayHi(greeting) :
	if greeting :
		print("hi")
	else :
		print("bye")
		
def sign(num):
	if num > 0 :
		print("+")
	elif num < 0 :
		print("-")
	else :
		print ("+/-")