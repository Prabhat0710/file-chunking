def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        factorial_of_n = 1
        for n in range(1, n + 1):
            factorial_of_n *= n
        return factorial_of_n
    

print(factorial(5))