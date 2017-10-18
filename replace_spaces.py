text = input("Ingrese texto:")
ch = input("ingrese caracter que reemplazara los espacios:")

modtext = ""
for c in text:
	if c == " ":
		modtext += ch
	else:
		modtext += c

print ("solucion 1: {0}".format(modtext))

modtext = ""
textitos = text.split(" ")
for t in range(0,len(textitos)):
	if t != len(textitos) - 1:
		modtext += textitos[t] + ch
	else:
		modtext += textitos[t]

print ("solucion 2: {0}".format(modtext))