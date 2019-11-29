def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)
numero = [] 
i = 0
for x in range(50): 
    i = i + 1
    numero.append(fib(x))
print(numero)
