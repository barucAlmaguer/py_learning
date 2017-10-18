#list = [3, 5, 4, -1, 10]

#j = 0
#for i in list :
#	print("v = " + str(i))
#	j+=1

#text = "hola mundo"
#for i in text :
#	print(i)

def mySplit(text, splitter) :
	splitted = text.split(splitter)
	print(splitted)

def myOtherSplit(text, splitter) :
	textList = []
	actTxt = ""
	for t in text :
		if (t != splitter) :
			actTxt += t
		else :
			textList.append(actTxt)
			actTxt = ""
	textList.append(actTxt)
	return textList
