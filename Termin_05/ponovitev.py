# https://kody.js.org/#-MyD6pditnCEiKmKaGPy

def some_function(a,b,c):
	temp = a*b+c
	print(temp)
	return temp

x = some_function(1,2,3)
print(x)


print()
def some_function(a,b,c):
	temp = a*b+c
	while 1<2:
		yield temp
		temp =  temp*2

gen = some_function(1,2,3)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

x = [ i for i in range(10)]
print()
print(x)
print(type(x))

x = { i for i in range(10)}
print()
print(x)
print(type(x))

x = [1,2,3,4,5]
x2 = [ el*2 for el in x]
print()
print(x2)
print(type(x2))
print()


def run_a_function(some_function_to_be_run):
	return some_function_to_be_run(10)

x = run_a_function(lambda x: x+1)
print(x)
print()

x = run_a_function(lambda x: x*2+x)
print(x)
print()

x = [1,2,3,3,4,67,89,90,2,3,3,0,9,1000,12,45,7]
print(sorted(x,key=lambda x: -x))


x = [ ("a",1), ("b",5),("nekaj",19), ("abc",-5) ]

print(sorted(x,key=lambda x: x[1],reverse=True))


