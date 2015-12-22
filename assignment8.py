
def fib() :
	a,b = 0,1
	while b > 0 :
		yield b
		a,b = b,a + b

f = fib()
print f.next()
