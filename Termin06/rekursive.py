# Python program to display the Fibonacci sequence
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


nterms = 10
fib = []
# check if the number of terms is valid
print("Fibonacci sequence:")
for i in range(nterms):
    fib.append(recur_fibo(i))
print(fib)
