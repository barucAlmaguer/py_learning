#funciones a decorar
def square(x):
	return x*x

def e(x):
	return 2.71**x
#funcion decoradora
def prettyfunction(f):
	def decf(x):
		val = f(x)
		fname = f.__name__
		s = "{}({}) = {}".format(fname, x, f(x))
		return s
	return decf


#decorando funciones:
prettysquare = prettyfunction(square)

#funcion sin decorar:
print("sin decorar:")
print(square(10))
#llamando funcion decorada:
print("decorada llamando funcion decoradora:")
print(prettysquare(10))

#decorando the python way:
@prettyfunction
def square(x):
	return x*x

#llamando funcion decorada in-situ:
print("decorada con @:")
print(square(10))
