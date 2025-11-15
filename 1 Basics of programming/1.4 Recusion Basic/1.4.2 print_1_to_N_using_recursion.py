# without any i counter
def print_1_to_n_using_rec(n):
    # Base condition
    if n == 0:
        return 
    print_1_to_n_using_rec(n-1)
    print(n,end=" ")
    

print(print_1_to_n_using_rec(4))