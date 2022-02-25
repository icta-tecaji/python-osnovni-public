# If stavki (FLOW CONTROL)
"""
if <expr>:
	<statement>
	<statement>
	<statement>
	<statement>
<following_statemen>
"""

a = 6
if a == 5:
	print("Sem znotraj if stavka")
print("Konec")
print()

if True:

                        print("Nekaj")
                        print("sdf")





a = 5
b = 6
if a < b:
	print("a<b")



a = 5
b = 6
c = 7

#if a < b > c:
if a<b and b>c:
	print("a<b>c")


a = 5
b = 6
if a == b:
	print("a je enak b-ju")
else:
	print("a ni enak b-ju")
print("Izven if-a")


"""
if <expr1>:
	<statements>
elif <expr2>:
	<statements>
elif <expr3>:
	<statements>
elif <expr4>:
	<statements>
else:
	<statements>
<following_statemen>
"""

print()
print()

x = 29
if x > 100:
    print('x je večje od 100')
elif x > 50:
    print('x večje od 50 in manjše od 100')
elif x > 30:
    print('x večje od 30 in manjše od 50')
elif x > 10:
    print('x večje od 10 in manjše od 30')
else:
    print("x manjše od 10")
print()

# z = <expr1> if <conditional_expr> else <expr2>

# if <conditional_expr>:
#	 z = <expr1>
# else:
# 	 z = <expr2>
x = 8
z = x+1 if x < 10 else x**2
print(z)


if (True):
	# TODO: naredi neko spremembo
	pass
print("nekajneakj")
















