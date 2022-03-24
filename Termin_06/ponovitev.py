# variable scope

a = 5
print(a)
print()

def fun1():
	a = 4
	print(a)
	print()
	fun2()
	print(a)

def fun2():
	# a = 3
	print(a)
	print()

fun1()


print(a)