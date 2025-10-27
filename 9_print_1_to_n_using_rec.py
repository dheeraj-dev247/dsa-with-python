def print_1_to_n_using_rec(n):
    # base condition
    if n == 0:
        return
    print_1_to_n_using_rec(n - 1)
    print(n, end=" ")


print_1_to_n_using_rec(5)
