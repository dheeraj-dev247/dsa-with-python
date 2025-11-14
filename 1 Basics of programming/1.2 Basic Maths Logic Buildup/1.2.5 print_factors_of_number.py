# There are three solution for this problem
# 1. Using loop
# 2. Using loop upto half of the number
# 3. Using sqrt

from math import sqrt

def print_factors_brute_force(num):
    result = []
    for i in range(1,num+1):
        if (num%i == 0):
            result.append(i)
    return result

print(print_factors_brute_force(36))


def print_factor_better_solution(num):
    n = num//2
    result = []
    for i in range(1,n+1):
        if (num%i == 0):
            result.append(i)
    result.append(num)
    return result

print(print_factor_better_solution(36))

def print_factor_optimal_solution(num):
    n = int(sqrt(num))
    result = []
    for i in range(1,n+1):
        if(num%i == 0):
            result.append(i)
            answer = num//i
            if(answer != i):
                result.append(answer)
    return result

print(print_factor_optimal_solution(48))