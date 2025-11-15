def find_factorial(n):
    #Base condition
    if n == 1:
        return 1
    return n * find_factorial(n-1)

print(find_factorial(5))