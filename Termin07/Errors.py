# stevila = [1, 3, 2, 0, 8, 4, "dan"]

# for stevilo in stevila:
#     try:
#         print(10 / stevilo)
#     except ZeroDivisionError:
#         print("deljenje z nic ni mogoce!")
#     except TypeError:
#         print("deliti moras s stevilom")
#     else:
#         print("deljenje je uspelo")
#     finally:
#         print(f"zelel si delit 10 s {stevilo}")

stevila = [1, 3, 2, 0, 8, 4]

for stevilo in stevila:
    try:
        if stevilo % 2 == 0:
            raise(ValueError("stevilo je sodo"))
        print(10 / stevilo)
    except ValueError as izjema:
        print(izjema)


