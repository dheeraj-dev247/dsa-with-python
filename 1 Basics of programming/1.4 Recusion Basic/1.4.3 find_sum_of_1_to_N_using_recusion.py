def sum_of_1_to_n(sum,i,n):
    #Base condition
    if i > n:
        return sum
    return sum_of_1_to_n(sum+i,i+1,n)


print(sum_of_1_to_n(0,1,3))