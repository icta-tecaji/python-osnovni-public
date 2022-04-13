# https://kody.js.org/#-N-T6M3S3PX_aQaRd6yX

class A:
	neki = 7
	def fun1(self, val):
		print(val)
class B(A):
	def fun1(self, val):
		# print(val,val)
		super().fun1(val)

var1 = B()
print(var1.neki)
print()

var1.fun1(5)
print()


try:
	a = 1/0
except:
	print("Prišlo je do napake!")

# a=1/0
print("jdsijdsf")























