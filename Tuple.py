emptyTuple = ()
singleItemTuple = ("spam", )
wrongSingleItemTuple = ("no comma")
thisTuple = 12, 89, 'a'
thatTuple = (12, 89, 'a')

print(emptyTuple)
print(singleItemTuple)
print(wrongSingleItemTuple)
print(thisTuple)
print(thatTuple)
print("thisTuple[1] = " + str(thisTuple[1]))

print("full tuple:")
for t in thisTuple :
	print (t)
	
ta = (1, 2, 3)
tb = (3, 4)
print (ta + tb)

#modifying a tuple:
tup = (1, 2)
print("tup= " + str(tup))
#OK:
tup = (3, 4)
print("tup= " + str(tup))
#No Ok:
#tup[1] = 5
#print("tup= " + str(tup))

#Tuple repetition
tupRep = ('a', 'c', 'x') * 3
print (tupRep)


#tuple returning function:
def minmax(list) :
	min = list[0]
	max = list[0]
	for e in list : 
		if e < min :
			min = e
		if e > max :
			max = e
	return min, max
