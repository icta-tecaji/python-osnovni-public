# a = [1,2,3,4,5,6,7,8,9]
# squares = []
# for i in a:
#     squares.append(i**2)

# print(squares)

a = [1,2,3,4,5,6,7,8,9]
squares = [i**2 for i in a]
print(squares)

even_squares = [i**2 for i in a if i%2==0]
print(even_squares)

a = {1,2,3,4,5,6}
even_squares = {i**2 for i in a if i%2==0}
print(even_squares)

dict_ = {"a":1, "b":2, "c":3, "d":4, "e":5}
squared_dict = {k:v**2 for (k,v) in dict_.items()}
print(squared_dict)

