def yielding(txt) :
	for char in txt :
		yield char.upper()

def squaring(num) :
	for i in range(1, num) :
		yield i * i
