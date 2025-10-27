def sum_of_series(n):
    if n == 1:
        return n
    return n**3 + sum_of_series(n - 1)


print(sum_of_series(3))
