temp = [
    1, 
    4, 
    [
        12,
        5,
        7
	],
    None,
    8
]

for i, x in enumerate(temp):
    print(i, x)
    # if isinstance(x,list):
    if i==2:
        for j, el in enumerate(x):
            print(el == x[j])
            print(">>>",j, el)

# def fun(a):
#     for x in temp:
#         if isinstance(x,list):
#             fun(a)
    
# fun([1,2,3])

# while True:
#     print(a)