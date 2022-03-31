# class SuperA:
#     VarA = 10
#     def funa(self):
#         return 11

# class SuperB:
#     VarB = 20
#     def funb(self):
#         return 21

# class Sub(SuperA, SuperB):
#     pass

# object_ = Sub()
# print(object_.VarA)
# print(object_.VarB)
# print(object_.funa())
# print(object_.funb())

# class A:
#     def fun(self):
#         return "a"

# class B:
#     def fun(self):
#         return "b"

# class C(B, A):
#     pass

# object_ = C()
# print(object_.fun())

class Level0:
    Var = 0
    def fun(self):
        return 0

class Level1(Level0):
    Var = 100
    def fun(self):
        return 101

class Level2(Level1):
    pass

# object_ = Level2()
# print(object_.Var)
# print(object_.fun())

# l0 = Level0()
# l1 = Level1()
# l2 = Level2()

# print(isinstance(l2, Level2))
# print(isinstance(l2, Level1))
# print(isinstance(l1, Level2))

import inspect

print(inspect.getmro(Level2))