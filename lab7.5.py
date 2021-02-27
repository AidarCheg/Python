def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
 
print(fib(int(input())))




#F3 = F2 + F1 = 1 + 1 = 2
#F4 = F3 + F2 = 2 + 1 = 3
#F5 = F4 + F3 = 3 + 2 = 5
#F6 = F5 + F4 = 5 + 3 = 8