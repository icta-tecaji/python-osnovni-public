# # Multiple inheritance


# class SuperA:
#     varA = 10

#     def funa(self):
#         return 11


# class SuperB:
#     varB = 20

#     def funb(self):
#         return 21


# class Sub(SuperA, SuperB):
#     pass

# obj = Sub()
# print(obj.varA, obj.funa())
# print(obj.varB, obj.funb())


# class A:
#     def fun(self):
#         return "a"


# class B:
#     def fun(self):
#         return "b"


# class C(A, B):  # prvo dedujemo od najbolj desnega
#     pass


# c = C()
# print(c.fun())


class Level0:
    var = 0

    def fun(self):
        return 0


class Level1(Level0):
    var = 100

    def fun(self):
        return 101


class Level2(Level1):
    pass
    # def neki(self):
    #     return super(Level1, self).fun()


obj = Level2()
# print(obj.var, obj.fun())
# print(obj.neki())

l0 = Level0()
l1 = Level1()
l2 = Level2()

print(isinstance(l2, Level2))
print(isinstance(l2, Level1))
print(isinstance(l2, Level0))
print(isinstance(l1, Level2))

import inspect

print(inspect.getmro(Level2))
